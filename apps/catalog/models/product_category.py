from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from apps.shared.models import BaseModel


class ProductCategory(BaseModel, TranslatableModel):
    slug = models.SlugField(
        verbose_name=_("Slug"),
        unique=True,
    )

    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children",
        verbose_name=_("Parent"),
    )

    translations = TranslatedFields(
        name=models.CharField(
            verbose_name=_("Name"),
            max_length=255,
            unique=True,
        )
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = _("Product Category")
        verbose_name_plural = _("Product Categories")

    def __str__(self):
        return self.safe_translation_getter("name", any_language=True)
