from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from apps.shared.models import BaseModel


class PromotionCategory(BaseModel, TranslatableModel):
    """Categories for organizing promotions (e.g., Seasonal, New Customer, Service-specific)"""

    slug = models.SlugField(
        verbose_name=_("Slug"),
        max_length=50,
        unique=True,
        help_text=_("URL-friendly identifier for the category"),
    )
    color = models.CharField(
        verbose_name=_("Color"),
        max_length=7,
        default="#FF6B35",
        help_text=_("Hex color code for category display"),
    )
    icon = models.CharField(
        verbose_name=_("Icon"),
        max_length=50,
        blank=True,
        null=True,
        help_text=_("Icon identifier for the category"),
    )
    is_active = models.BooleanField(
        verbose_name=_("Is Active"),
        default=True,
        help_text=_("Whether this category is currently active"),
    )
    display_order = models.SmallIntegerField(
        verbose_name=_("Display Order"),
        default=1,
        help_text=_("Order in which the category is displayed"),
    )

    translations = TranslatedFields(
        name=models.CharField(
            verbose_name=_("Name"),
            max_length=100,
            help_text=_("The name of the promotion category"),
        ),
        description=models.TextField(
            verbose_name=_("Description"),
            blank=True,
            null=True,
            help_text=_("Optional description of the category"),
        ),
    )

    class Meta:
        ordering = ["display_order", "created"]
        verbose_name = _("Promotion Category")
        verbose_name_plural = _("Promotion Categories")

    def __str__(self):
        return self.safe_translation_getter("name", any_language=True)