from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.shared.models import BaseModel


class Wish(BaseModel):
    profile = models.ForeignKey(
        to="accounts.Profile",
        on_delete=models.CASCADE,
        related_name="wishes",
        verbose_name=_("Profile"),
    )
    product = models.ForeignKey(
        to="catalog.Product",
        on_delete=models.CASCADE,
        related_name="wished_by",
        verbose_name=_("Product"),
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = _("Wish")
        verbose_name_plural = _("Wishes")
        unique_together = ("profile", "product")

    def __str__(self):
        return f"{self.profile} -> {self.product}"
