from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.shared.models import BaseModel


class Order(BaseModel):
    profile = models.ForeignKey(
        to="accounts.Profile",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
        verbose_name=_("Profile"),
    )

    name = models.CharField(
        verbose_name=_("Name"),
        max_length=40,
    )

    phone = models.CharField(
        verbose_name=_("Phone"),
        max_length=13,
    )

    email = models.EmailField(
        verbose_name=_("Email"),
        max_length=50,
        blank=True,
        null=True,
    )

    is_processed = models.BooleanField(
        verbose_name=_("Is Processed"),
        default=False,
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return f"Order {self.id} by {self.name}"
