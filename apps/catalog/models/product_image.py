from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.shared.models import BaseModel


class ProductImage(BaseModel):
    product = models.ForeignKey(
        to="catalog.Product",
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name=_("Product"),
    )

    is_main = models.BooleanField(
        verbose_name=_("Is Main"),
        default=False,
    )

    photo = models.ImageField(
        verbose_name=_("Photo"),
        upload_to="product_images/",
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")

    def __str__(self):
        return str(self.product)
