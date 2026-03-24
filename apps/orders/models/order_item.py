from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.shared.models import BaseModel


class OrderItem(BaseModel):
    order = models.ForeignKey(
        to="orders.Order",
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name=_("Order"),
    )

    product = models.ForeignKey(
        to="catalog.Product",
        on_delete=models.CASCADE,
        related_name="order_items",
        verbose_name=_("Product"),
    )

    quantity = models.PositiveIntegerField(
        verbose_name=_("Quantity"),
        default=1,
    )

    price = models.IntegerField(
        verbose_name=_("Price"),
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")
        unique_together = ("order", "product")

    def __str__(self):
        return f"{self.quantity} x {self.product} in {self.order}"
