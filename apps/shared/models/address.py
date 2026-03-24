from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from apps.shared.models import BaseModel


class Address(BaseModel, TranslatableModel):
    langitude = models.FloatField(
        verbose_name=_("Longitude"),
        help_text=_("Longitude of the address"),
    )
    lattitude = models.FloatField(
        verbose_name=_("Latitude"),
        help_text=_("Latitude of the address"),
    )

    translations = TranslatedFields(
        text=models.CharField(
            verbose_name=_("Text"),
            max_length=255,
            help_text=_("The text representation of the address"),
        ),
        name=models.CharField(
            verbose_name=_("Name"),
            max_length=255,
            blank=True,
            null=True,
            help_text=_("Optional name of the address"),
        ),
    )

    class Meta:
        ordering = ["created"]
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")

    def __str__(self):
        return self.safe_translation_getter("name", any_language=True) or self.safe_translation_getter("text", any_language=True)
