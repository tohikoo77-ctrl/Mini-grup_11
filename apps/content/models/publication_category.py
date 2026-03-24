from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from apps.shared.models import BaseModel


class PublicationCategory(BaseModel, TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(
            verbose_name=_("Name"),
            max_length=255,
            unique=True,
        )
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = _("Publication Category")
        verbose_name_plural = _("Publication Categories")

    def __str__(self):
        return self.safe_translation_getter("name", any_language=True)
