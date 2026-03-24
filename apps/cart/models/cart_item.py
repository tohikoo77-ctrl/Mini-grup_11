from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.shared.models import BaseModel


class CartItem(BaseModel):
    cart = models.ForeignKey(
        to="cart.Cart",
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name=_("Cart"),
    )

    product = models.ForeignKey(
        to="catalog.Product",
        on_delete=models.CASCADE,
        related_name="cart_items",
        verbose_name=_("Product"),
    )

    quantity = models.PositiveIntegerField(
        verbose_name=_("Quantity"),
        default=1,
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = _("Cart Item")
        verbose_name_plural = _("Cart Items")
        unique_together = ("cart", "product")

    def __str__(self):
        return f"{self.quantity} x {self.product} in {self.cart}"
