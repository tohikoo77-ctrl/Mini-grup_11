import random
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from apps.shared.models import BaseModel
from apps.shared.validators import validate_password, validate_username, validate_email_lower, phone_regex
from ..managers import UserManager
from ...shared.enums import AuthStatuses, AuthTypes


class User(AbstractUser, BaseModel):
    # Completely remove them
    first_name = None
    last_name = None

    # Restore the email field and make it unique but nullable
    email = models.EmailField(
        validators=[validate_email_lower],
        null=True,
        blank=True,
    )

    # Add a nullable phone field, unique but nullable
    phone = models.CharField(
        max_length=13,
        validators=[phone_regex],
        null=True,
        blank=True,
    )

    auth_status = models.CharField(
        max_length=31,
        choices=AuthStatuses.choices,
        default=AuthStatuses.NEW,
    )

    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[validate_username],
    )

    password = models.CharField(
        max_length=128,
        validators=[validate_password],
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []  # No required fields during initial creation

    objects = UserManager()

    def __str__(self):
        return self.username or self.email or self.phone or f"user-{self.id}"

    def token(self):
        from rest_framework_simplejwt.tokens import RefreshToken
        refresh = RefreshToken.for_user(self)
        return {
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
        }