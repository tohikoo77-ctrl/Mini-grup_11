import random
import string

from django.db.models import Q
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.validators import FileExtensionValidator, validate_email
from icecream import ic

from apps.shared.enums import AuthStatuses, AuthTypes, Genders
from apps.shared.utils.verification import VerificationService
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.exceptions import ValidationError, PermissionDenied, NotFound
from django.utils.translation import gettext_lazy as _

from apps.shared.utility import check_username_phone_email, send_email, send_phone_code, check_user_type, phone_regex
from .models import Profile, User, UserConfirmation

# --------------------
# Profile Nested Serializers
# --------------------
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"



# --------------------
# User Response Serializer (output)
# --------------------
from rest_framework import serializers
from apps.accounts.models import User  # adjust import if needed

class UserResponseSerializer(serializers.ModelSerializer):
    # Profile fields
    full_name = serializers.CharField(source="profile.full_name", read_only=True)
    gender = serializers.CharField(source="profile.gender", read_only=True)
    birth_date = serializers.DateField(source="profile.birth_date", read_only=True)
    avatar_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "last_login",
            "is_superuser",
            "is_staff",
            "is_active",
            "date_joined",
            "created",
            "modified",
            "email",
            "phone",
            "auth_status",
            "username",
            "full_name",
            "gender",
            "birth_date",
            "avatar_url",
        ]

    def get_avatar_url(self, obj):
        if obj.profile.avatar:
            request = self.context.get("request")
            url = obj.profile.avatar.url
            if request:
                return request.build_absolute_uri(url)
            return url
        return None

# --------------------
# SignUp Serializer (main)
# --------------------
class SignUpSerializer(serializers.Serializer):
    username_phone_email = serializers.CharField(required=True, write_only=True)

    # internal fields (set in validate, not provided by client)
    verify_type = serializers.CharField(read_only=True)
    verify_value = serializers.CharField(read_only=True)

    def create(self, validated_data):
        verify_type = validated_data.get("verify_type")
        verify_value = validated_data.get("verify_value")

        if not verify_type or not verify_value:
            raise ValidationError({"message": "verify_type or verify_value missing"})

        from apps.accounts.views import PasswordGeneratorView
        password_response = PasswordGeneratorView.generate_password()
        password = password_response["password"]

        username = self.generate_username()

        user = User(username=username)
        user.set_password(password)

        user.save()

        VerificationService.create_and_send_code(
            user=user,
            verify_type=verify_type,
            verify_value=verify_value
        )

        return user

    @staticmethod
    def generate_username(length: int = 8):
        letters_digits = string.ascii_lowercase + string.digits
        return "user_" + "".join(random.choices(letters_digits, k=length))

    def validate(self, data):
        data = super().validate(data)
        return self.auth_validate(data)

    @staticmethod
    def auth_validate(data):
        user_input = str(data.get("username_phone_email")).lower()
        input_type = check_username_phone_email(user_input)

        if input_type == "email":
            try:
                validate_email(user_input)
            except ValidationError:
                raise ValidationError({"message": "Invalid email address"})
            data["verify_type"] = AuthTypes.VIA_EMAIL
            data["verify_value"] = user_input

        elif input_type == "phone":
            if not phone_regex.match(user_input):
                raise ValidationError({"message": "Invalid phone number format"})
            data["verify_type"] = AuthTypes.VIA_PHONE
            data["verify_value"] = user_input

        else:
            raise ValidationError({"message": "You must send a valid email or phone number"})

        return data

    def to_representation(self, instance):
        return {
                "user": UserResponseSerializer(instance).data,
                "next_step": str(_("Verify code sent to your email or phone")),
                **(instance.token() if callable(getattr(instance, "token", None)) else {})
            }

from rest_framework import serializers
from apps.shared.enums import AuthStatuses

class UpdateUserInformation(serializers.Serializer):
    # User fields
    username = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    # Profile fields
    full_name = serializers.CharField(write_only=True, required=True)
    gender = serializers.ChoiceField(
        write_only=True,
        required=True,
        choices=Genders.choices,
    )
    birth_date = serializers.DateField(write_only=True, required=True)
    avatar = serializers.ImageField(required=False, allow_null=True, write_only=True)

    # Read-only field for response
    avatar_url = serializers.SerializerMethodField(read_only=True)

    def get_avatar_url(self, obj):
        # obj → User instance
        if obj.profile.avatar:
            request = self.context.get("request")
            avatar_url = obj.profile.avatar.url
            if request:
                return request.build_absolute_uri(avatar_url)
            return avatar_url
        return None

    def validate(self, data):
        password = data.get("password")
        confirm_password = data.get("confirm_password")

        if password != confirm_password:
            raise serializers.ValidationError(
                {"message": "Parolingiz va tasdiqlash parolingiz bir-biriga teng emas"}
            )
        if password:
            validate_password(password)

        return data

    def validate_username(self, username):
        if len(username) < 5 or len(username) > 30:
            raise serializers.ValidationError(
                {"message": "Username must be between 5 and 30 characters long"}
            )
        if username.isdigit():
            raise serializers.ValidationError(
                {"message": "This username is entirely numeric"}
            )
        return username

    def update(self, instance, validated_data):
        # Update User
        instance.username = validated_data.get("username", instance.username)
        if validated_data.get("password"):
            instance.set_password(validated_data["password"])

        # Update Profile
        profile = instance.profile
        profile.full_name = validated_data.get("full_name", profile.full_name)
        profile.gender = validated_data.get("gender", profile.gender)
        profile.birth_date = validated_data.get("birth_date", profile.birth_date)

        avatar = validated_data.get("avatar")
        if avatar is not None:  # update only if provided
            profile.avatar = avatar

        profile.save()

        # Update auth_status if needed
        if instance.auth_status == AuthStatuses.CODE_VERIFIED:
            instance.auth_status = AuthStatuses.DONE

        instance.save()
        return instance

class LoginSerializer(TokenObtainPairSerializer):

    def __init__(self, *args, **kwargs):
        super(LoginSerializer, self).__init__(*args, **kwargs)
        self.fields['userinput'] = serializers.CharField(required=True)
        self.fields['username'] = serializers.CharField(required=False, read_only=True)

    def get_user(self, **kwargs):
        """
        Get user by provided filter kwargs
        """
        try:
            return User.objects.get(**kwargs)
        except User.DoesNotExist:
            data = {
                'success': False,
                'message': "Bunday foydalanuvchi topilmadi"
            }
            raise ValidationError(data)
        except User.MultipleObjectsReturned:
            data = {
                'success': False,
                'message': "Bir nechta foydalanuvchi topildi"
            }
            raise ValidationError(data)

    def auth_validate(self, data):
        user_input = data.get('userinput')  # email, phone, username

        if check_user_type(user_input) == 'username':
            username = user_input
        elif check_user_type(user_input) == "email":  # Anora@gmail.com -> anOra@gmail.com
            user = self.get_user(email__iexact=user_input)
            username = user.username
        elif check_user_type(user_input) == 'phone':
            user = self.get_user(phone=user_input)
            username = user.username
        else:
            data = {
                'success': False,
                'message': "Siz email, username yoki telefon raqami jonatishingiz kerak"
            }
            raise ValidationError(data)

        authentication_kwargs = {
            self.username_field: username,
            'password': data['password']
        }

        # user statusi tekshirilishi kerak
        current_user = User.objects.filter(username__iexact=username).first()

        if current_user is not None and current_user.auth_status in [AuthStatuses.NEW, AuthStatuses.CODE_VERIFIED]:
            raise ValidationError(
                {
                    'message': "Siz royhatdan toliq otmagansiz!"
                }
            )

        user = authenticate(**authentication_kwargs)
        if user is not None:
            self.user = user
        else:
            raise ValidationError({
                'message': "The login or password you entered is incorrect. Please check and try again."
            })

    def validate(self, data):
        self.auth_validate(data)
        if self.user.auth_status not in [AuthStatuses.DONE]:  # Fixed duplicate status
            raise PermissionDenied("Siz login qila olmaysiz. Ruxsatingiz yoq")
        data = self.user.token()
        data['auth_status'] = self.user.auth_status
        return data

class LoginRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        try:
            refresh = RefreshToken(attrs['refresh'])
        except TokenError:
            raise ValidationError({'refresh': "Token noto'g'ri yoki muddati tugagan"})

        data = {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }
        return data


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    class JSONAPIMeta:
        resource_name = "logout"


class ResetPasswordSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    password = serializers.CharField(min_length=8, required=True, write_only=True)
    confirm_password = serializers.CharField(min_length=8, required=True, write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'password',
            'confirm_password'
        )

    def validate(self, data):
        password = data.get('password', None)
        confirm_password = data.get('password', None)
        if password != confirm_password:
            raise ValidationError(
                {
                    'success': False,
                    'message': "Parollaringiz qiymati bir-biriga teng emas"
                }
            )
        if password:
            validate_password(password)
        return data

    def update(self, instance, validated_data):
        password = validated_data.pop('password')
        instance.set_password(password)
        return super(ResetPasswordSerializer, self).update(instance, validated_data)

class ForgotPasswordSerializer(serializers.Serializer):
    email_or_phone = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        email_or_phone = attrs.get('email_or_phone', None)
        if email_or_phone is None:
            raise ValidationError(
                {
                    "success": False,
                    'message': "Email yoki telefon raqami kiritilishi shart!"
                }
            )
        user = User.objects.filter(Q(phone=email_or_phone) | Q(email=email_or_phone))
        if not user.exists():
            raise NotFound(detail="User not found")
        attrs['user'] = user.first()
        return attrs