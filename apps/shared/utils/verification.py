import datetime
import random

from django.utils import timezone
from icecream import ic

from apps.accounts.models import UserConfirmation
from apps.shared.enums import AuthTypes
from apps.shared.utility import send_email, send_phone_code


class VerificationService:
    CODE_LENGTH = 4
    CODE_EXPIRY_MINUTES = 2

    @staticmethod
    def _generate_code(length: int = CODE_LENGTH) -> str:
        """Generate a numeric code of given length."""
        return str(random.randint(10**(length - 1), 10**length - 1))

    @classmethod
    def create_and_send_code(cls, user, verify_type, verify_value):
        """
        Create a confirmation code for the user and send it via email or phone.
        """
        # Remove old confirmations for the same type/value
        UserConfirmation.objects.filter(
            user=user,
            verify_type=verify_type,
            verify_value=verify_value,
            is_confirmed=False,
            expires_at__gt=timezone.now(),
        ).delete()

        # Generate code
        code = cls._generate_code()

        # Create confirmation record
        confirmation = UserConfirmation.objects.create(
            user=user,
            verify_type=verify_type,
            verify_value=verify_value,
            code=code,
            is_confirmed=False,
            expires_at=timezone.now() + datetime.timedelta(minutes=cls.CODE_EXPIRY_MINUTES),
        )

        # Send code
        if verify_type == AuthTypes.VIA_EMAIL:
            send_email(verify_value, code)
        elif verify_type == AuthTypes.VIA_PHONE:
            send_phone_code(verify_value, code)

        return confirmation  # don't return the code for security
