from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.shared.models import BaseModel


class Promotion(BaseModel):

    class DiscountType(models.TextChoices):
        PERCENT = "percent", _("Percent")
        FIXED = "fixed", _("Fixed")

    title = models.CharField(
        verbose_name=_("Title"),
        max_length=100,
        blank=True,
        null=True,
    )

    discount_type = models.CharField(
        verbose_name=_("Discount Type"),
        max_length=10,
        choices=DiscountType.choices,
        blank=True,
        null=True,
    )

    discount_value = models.IntegerField(
        verbose_name=_("Discount Value"),
        blank=True,
        null=True,
    )

    expires_at_date = models.DateField(
        verbose_name=_("Expires At"),
        blank=True,
        null=True,
    )

    coupon_code = models.CharField(
        verbose_name=_("Coupon Code"),
        max_length=9,
        unique=True,
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = _("Promotion")
        verbose_name_plural = _("Promotions")

    def __str__(self):
        return self.title or str(self.id)
