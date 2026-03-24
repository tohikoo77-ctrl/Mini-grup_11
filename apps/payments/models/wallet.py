from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.shared.models import BaseModel


class Wallet(BaseModel):
    profile = models.ForeignKey(
        to="accounts.Profile",
        on_delete=models.CASCADE,
        related_name="wallets",
        verbose_name=_("Profile"),
        help_text=_("The profile this wallet belongs to"),
    )
    balance = models.IntegerField(
        verbose_name=_("Balance"),
        default=0,
        help_text=_("Current balance of the wallet"),
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = _("Wallet")
        verbose_name_plural = _("Wallets")

    def __str__(self):
        return f"Wallet of {self.profile} with balance {self.balance}"
