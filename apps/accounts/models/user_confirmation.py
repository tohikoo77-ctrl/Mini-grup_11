from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from apps.shared.models import BaseModel
from apps.shared.enums import AuthTypes


class UserConfirmation(BaseModel):
    code = models.CharField(
        verbose_name=_("Code"),
        max_length=255,
        help_text=_("The verification code"),
    )
    verify_type = models.CharField(
        verbose_name=_("Verify Type"),
        max_length=20,
        choices=AuthTypes.choices,
        default=AuthTypes.VIA_PHONE,
        help_text=_("The type of verification (phone or email)"),
    )
    verify_value = models.CharField(
        verbose_name=_("Verify Value"),
        max_length=255,
        help_text=_("Phone number or email to verify"),
    )
    user = models.ForeignKey(
        to="accounts.User",
        on_delete=models.CASCADE,
        related_name="confirmations",
        verbose_name=_("User"),
        help_text=_("The user to confirm"),
    )
    expires_at = models.DateTimeField(
        verbose_name=_("Expires At"),
        help_text=_("Expiration datetime of the confirmation code"),
    )
    is_confirmed = models.BooleanField(
        verbose_name=_("Is Confirmed"),
        default=False,
        help_text=_("Whether the user has confirmed"),
    )
    confirmed_at = models.DateTimeField(
        verbose_name=_("Confirmed At"),
        blank=True,
        null=True,
        help_text=_("Timestamp when the confirmation was completed"),
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = _("User Confirmation")
        verbose_name_plural = _("User Confirmations")

    def __str__(self):
        return f"Confirmation for {self.user} via {self.verify_type}"
