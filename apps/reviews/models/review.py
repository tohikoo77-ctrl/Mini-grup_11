from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.shared.models import BaseModel


class Review(BaseModel):
    profile = models.ForeignKey(
        to="accounts.Profile",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reviews",
        verbose_name=_("Profile"),
    )

    product = models.ForeignKey(
        to="catalog.Product",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reviews",
        verbose_name=_("Product"),
    )

    text = models.CharField(
        verbose_name=_("Text"),
        max_length=1000,
    )

    rating = models.PositiveSmallIntegerField(
        verbose_name=_("Rating"),
    )

    is_approved = models.BooleanField(
        verbose_name=_("Is Approved"),
        default=False,
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")

    def __str__(self):
        return f"Review by {self.profile} for {self.product}"
