from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.shared.models import BaseModel


class DiscountThreshold(BaseModel):
    min_amount = models.DecimalField(
        verbose_name=_("Minimum Amount"),
        max_digits=10,
        decimal_places=2,
    )

    discount_percent = models.PositiveSmallIntegerField(
        verbose_name=_("Discount Percent"),
    )

    active = models.BooleanField(
        verbose_name=_("Active"),
        default=True,
    )

    class Meta:
        ordering = ["-min_amount"]
        verbose_name = _("Discount Threshold")
        verbose_name_plural = _("Discount Thresholds")

    def __str__(self):
        return f"{self.discount_percent}% for {self.min_amount}"
