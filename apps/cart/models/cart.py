from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.shared.models import BaseModel


class Cart(BaseModel):
    profile = models.ForeignKey(
        to="accounts.Profile",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="carts",
        verbose_name=_("Profile"),
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = _("Cart")
        verbose_name_plural = _("Carts")

    def __str__(self):
        return f"Cart {self.id} for {self.profile}"
