from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from apps.shared.models import BaseModel


class Color(BaseModel, TranslatableModel):
    hex_code = models.CharField(
        verbose_name=_("HEX Code"),
        max_length=7,
        blank=True,
        null=True,
    )

    rgb_value = models.CharField(
        verbose_name=_("RGB Value"),
        max_length=50,
        blank=True,
        null=True,
    )

    hsl_value = models.CharField(
        verbose_name=_("HSL Value"),
        max_length=50,
        blank=True,
        null=True,
    )

    translations = TranslatedFields(
        name=models.CharField(
            verbose_name=_("Name"),
            max_length=100,
        )
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = _("Color")
        verbose_name_plural = _("Colors")

    def __str__(self):
        return self.safe_translation_getter("name", any_language=True)
