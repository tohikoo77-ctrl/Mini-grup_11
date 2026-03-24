from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from apps.shared.models import BaseModel


class Product(BaseModel, TranslatableModel):

    class ProductTypes(models.TextChoices):
        KIT = "kit", _("Kit")
        STAND = "stand", _("Stand")
        ADAPTER = "adapter", _("Adapter")
        FILTER = "filter", _("Filter")

    class MotorTypes(models.TextChoices):
        BRUSHED = "brushed", _("Brushed")

    class ChuckTypes(models.TextChoices):
        KEYLESS = "keyless", _("Keyless")

    category = models.ForeignKey(
        to="catalog.ProductCategory",
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name=_("Category"),
    )

    brand = models.ForeignKey(
        to="catalog.Brand",
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name=_("Brand"),
    )

    color = models.ForeignKey(
        to="catalog.Color",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
        verbose_name=_("Color"),
    )

    material = models.ForeignKey(
        to="catalog.Material",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
        verbose_name=_("Material"),
    )

    code = models.CharField(
        verbose_name=_("Code"),
        max_length=8,
        unique=True,
        null=True,
        blank=True,
    )

    price = models.IntegerField(
        verbose_name=_("Price"),
    )

    type = models.CharField(
        verbose_name=_("Product Type"),
        max_length=20,
        choices=ProductTypes.choices,
        null=True,
        blank=True,
    )

    power = models.SmallIntegerField(
        verbose_name=_("Power"),
        null=True,
        blank=True,
    )

    capacity = models.DecimalField(
        verbose_name=_("Capacity"),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )

    max_torque = models.SmallIntegerField(
        verbose_name=_("Max Torque"),
        null=True,
        blank=True,
    )

    battery_voltage = models.DecimalField(
        verbose_name=_("Battery Voltage"),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )

    weight = models.DecimalField(
        verbose_name=_("Weight"),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )

    motor_type = models.CharField(
        verbose_name=_("Motor Type"),
        max_length=20,
        choices=MotorTypes.choices,
        null=True,
        blank=True,
    )

    chuck_type = models.CharField(
        verbose_name=_("Chuck Type"),
        max_length=20,
        choices=ChuckTypes.choices,
        null=True,
        blank=True,
    )

    translations = TranslatedFields(
        title=models.CharField(
            verbose_name=_("Title"),
            max_length=255,
        ),
        description=models.TextField(
            verbose_name=_("Description"),
            blank=True,
            null=True,
        ),
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True)
