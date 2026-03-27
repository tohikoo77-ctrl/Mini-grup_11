from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from apps.shared.models import BaseModel
from apps.shared.enums import PaymentStatuses


class Payment(BaseModel):
    profile = models.ForeignKey(
        to="accounts.Profile",
        on_delete=models.CASCADE,
        related_name="payments",
        verbose_name=_("Profile"),
        help_text=_("The profile that made the payment"),
    )
    amount = models.IntegerField(
        verbose_name=_("Amount"),
        help_text=_("The amount of the payment"),
    )
    payment_type = models.ForeignKey(
        to="payments.PaymentType",
        on_delete=models.CASCADE,
        related_name="payments",
        verbose_name=_("Payment Type"),
        help_text=_("The type/method of the payment"),
    )
    paid_at = models.DateTimeField(
        verbose_name=_("Paid At"),
        blank=True,
        null=True,
        help_text=_("Timestamp when the payment was made"),
    )
    reviewed_by = models.ForeignKey(
        to="accounts.Profile",
        on_delete=models.CASCADE,
        related_name="payments_reviewed",
        verbose_name=_("Reviewed By"),
        help_text=_("Profile who reviewed the payment"),
    )
    reviewed_at = models.DateTimeField(
        verbose_name=_("Reviewed At"),
        blank=True,
        null=True,
        help_text=_("Timestamp when the payment was reviewed"),
    )
    status = models.CharField(
        verbose_name=_("Status"),
        max_length=20,
        choices=PaymentStatuses.choices,
        default=PaymentStatuses.PENDING,
        help_text=_("Current status of the payment"),
    )
    receipt = models.FileField(
        verbose_name=_("Receipt"),
        upload_to="payments/receipts/",
        blank=True,
        null=True,
        help_text=_("Uploaded receipt file"),
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = _("Payment")
        verbose_name_plural = _("Payments")

    def __str__(self):
        return f"Payment {self.id} by {self.profile}"
