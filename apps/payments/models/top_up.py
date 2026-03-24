from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.shared.models import BaseModel


class TopUp(BaseModel):
    profile = models.ForeignKey(
        to="accounts.Profile",
        on_delete=models.CASCADE,
        related_name="top_ups",
        verbose_name=_("Profile"),
        help_text=_("The profile that performed the top-up"),
    )
    amount = models.PositiveIntegerField(
        verbose_name=_("Amount"),
        help_text=_(
            "Allowed amounts: 5.000, 10.000, 20.000, 25.000, 50.000, 75.000, "
            "100.000, 200.000 or a custom amount"
        ),
    )
    payment = models.ForeignKey(
        to="payments.Payment",
        on_delete=models.CASCADE,
        related_name="top_ups",
        verbose_name=_("Payment"),
        help_text=_("The payment associated with this top-up"),
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = _("Top-Up")
        verbose_name_plural = _("Top-Ups")

    def __str__(self):
        return f"{self.profile} topped up {self.amount}"
