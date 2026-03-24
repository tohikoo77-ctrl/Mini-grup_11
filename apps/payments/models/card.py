from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.shared.models import BaseModel


class Card(BaseModel):
    wallet = models.ForeignKey(
        to="payments.Wallet",
        on_delete=models.CASCADE,
        related_name="cards",
        verbose_name=_("Wallet"),
        help_text=_("The wallet this card belongs to"),
    )
    number = models.CharField(
        verbose_name=_("Card Number"),
        max_length=16,
        unique=True,
        help_text=_("16-digit card number"),
    )
    account_holder_name = models.CharField(
        verbose_name=_("Account Holder Name"),
        max_length=255,
        help_text=_("The name of the cardholder"),
    )
    expires_at = models.DateTimeField(
        verbose_name=_("Expires At"),
        help_text=_("The expiry date of the card"),
    )
    cvv = models.SmallIntegerField(
        verbose_name=_("CVV"),
        help_text=_("3-digit security code on the card"),
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = _("Card")
        verbose_name_plural = _("Cards")

    def __str__(self):
        return f"{self.account_holder_name} - ****{self.number[-4:]}"
