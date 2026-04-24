from django.utils import timezone, translation
from django.utils.translation import gettext_lazy as _

from apps.shared.utils.verification import VerificationService
from rest_framework import permissions, status, generics
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.generics import CreateAPIView, UpdateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.decorators import api_view

from icecream import ic

from apps.shared.utility import send_email, check_username_phone_email, send_phone_code
from .serializers import SignUpSerializer, UpdateUserInformation, LoginSerializer, \
    LoginRefreshSerializer, LogoutSerializer, ResetPasswordSerializer, ForgotPasswordSerializer, ProfileSerializer, UserResponseSerializer
from .models import Profile, User, UserConfirmation
from ..shared.enums import AuthTypes, AuthStatuses


class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = SignUpSerializer

    def create(self, request, *args, **kwargs):
        # Use the serializer to validate and create the user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Return the serializer's custom representation (user + tokens)
        data = serializer.to_representation(user)
        return Response(data, status=status.HTTP_201_CREATED)

class VerifyAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        user = request.user
        code = request.data.get('code')
        self.check_verify(user, code)
        token = user.token()
        return Response({
            "auth_status": user.auth_status,
            "access_token": token['access_token'],
            "refresh": token['refresh_token']
        })

    @staticmethod
    def check_verify(user, code):
        verification = user.confirmations.filter(
            expires_at__gte=timezone.now(),
            code=code,
            is_confirmed=False
        ).first()

        if not verification:
            raise ValidationError({
                "message": _("Tasdiqlash kodingiz xato yoki eskirgan")
            })

        verification.is_confirmed = True
        verification.confirmed_at = timezone.now()
        verification.save()
        ic(user.auth_status, AuthStatuses.NEW)

        if user.auth_status == AuthStatuses.NEW:
            user.auth_status = AuthStatuses.CODE_VERIFIED

        if verification.verify_type == AuthTypes.VIA_EMAIL:
            user.email = verification.verify_value
        elif verification.verify_type == AuthTypes.VIA_PHONE:
            user.phone = verification.verify_value

        user.save()
        return True

class GetNewVerification(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        user = request.user

        # Grab the latest unconfirmed user confirmation
        confirmation = (
            user.confirmations  # assumes related_name="confirmations"
            .filter(is_confirmed=False)
            .order_by("-created")  # newest first
            .first()
        )
        ic(confirmation)

        if not confirmation:
            raise ValidationError({"message": "No active verification found for this user."})

        # Prevent spamming new codes if one is still valid
        self.check_verification(user)

        # Decide channel
        VerificationService.create_and_send_code(
            user=user,
            verify_type=confirmation.verify_type,
            verify_value=confirmation.verify_value
        )

        return Response(
            {
                "message": _("Tasdiqlash kodingiz qaytadan jo'natildi.")
            }
        )

    @staticmethod
    def check_verification(user):
        verifies = user.confirmations.filter(
            expires_at__gte=timezone.now(),
            is_confirmed=False
        )
        if verifies.exists():
            raise ValidationError(
                {"message": _("Kodingiz hali ishlatish uchun yaroqli. Biroz kutib turing")}
            )

class UpdateUserInformationView(UpdateAPIView):
    serializer_class = UpdateUserInformation
    http_method_names = ("patch", "put")
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(instance=user, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserResponseSerializer(user).data, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(instance=user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserResponseSerializer(user).data, status=status.HTTP_200_OK)

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

class LoginRefreshView(TokenRefreshView):
    serializer_class = LoginRefreshSerializer

class LogOutView(APIView):
    serializer_class = LogoutSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        refresh_token = serializer.validated_data["refresh"]

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {
                    "data": {
                        "type": "logout",
                        "attributes": {
                            "success": True,
                            "message": "You have been logged out."
                        }
                    }
                },
                status=status.HTTP_200_OK,
            )

        except TokenError:
            raise ValidationError({
                "refresh": "Token is invalid or expired."
            })

class ForgotPasswordView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = ForgotPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        email_or_phone = serializer.validated_data.get('email_or_phone')
        user = serializer.validated_data.get('user')

        input_type = check_username_phone_email(email_or_phone)
        VerificationService.create_and_send_code(
            user=user,
            verify_type=f"via_{input_type}",
            verify_value=email_or_phone
        )

        return Response(
            {
                "success": True,
                'message': "Tasdiqlash kodi muvaffaqiyatli yuborildi",
                "access": user.token()['access_token'],
                "refresh": user.token()['refresh_token'],
                "user_status": user.auth_status,
            }, status=200
        )

class ResetPasswordView(UpdateAPIView):
    serializer_class = ResetPasswordSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ('put',)

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        response = super(ResetPasswordView, self).update(request, *args, **kwargs)
        try:
            user = User.objects.get(id=response.data.get('id'))
        except:
            raise NotFound(detail='User not found')
        return Response(
            {
                'success': True,
                'message': "Parolingiz muvaffaqiyatli o'zgartirildi",
                'access': user.token()['access_token'],
                'refresh': user.token()['refresh_token'],
            }
        )

class PasswordGeneratorView(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def generate_password(
        length=12,
        include_upper=True,
        include_lower=True,
        include_digits=True,
        include_symbols=False,
    ):
        import random, string

        if length < 8:
            raise ValueError("Minimum password length is 8.")

        charset = ''
        if include_upper:
            charset += string.ascii_uppercase
        if include_lower:
            charset += string.ascii_lowercase
        if include_digits:
            charset += string.digits
        if include_symbols:
            charset += string.punctuation

        if not charset:
            raise ValueError("No character sets selected.")

        password = ''.join(random.SystemRandom().choice(charset) for _ in range(length))
        return {"password": password}

    def get(self, request):
        length = int(request.query_params.get('length', 12))
        include_upper = request.query_params.get('upper', 'true') == 'true'
        include_lower = request.query_params.get('lower', 'true') == 'true'
        include_digits = request.query_params.get('digits', 'true') == 'true'
        include_symbols = request.query_params.get('symbols', 'false') == 'true'

        try:
            result = self.generate_password(
                length=length,
                include_upper=include_upper,
                include_lower=include_lower,
                include_digits=include_digits,
                include_symbols=include_symbols,
            )
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(result, status=status.HTTP_200_OK)


@api_view(['GET'])
def test_login(request):
    # Get user's language preference
    user_language = request.user.profile.app_language.code
    ic(user_language)

    # Activate the user's language directly
    translation.activate(user_language)

    # Now gettext will use the activated language
    ic(_("Hello, world!"))
    return Response({"message": _("Hello, world!")})
