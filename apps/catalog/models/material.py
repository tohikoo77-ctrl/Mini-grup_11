from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from apps.shared.models import BaseModel


class Material(BaseModel, TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(
            verbose_name=_("Title"),
            max_length=255,
            unique=True,
        )
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = _("Material")
        verbose_name_plural = _("Materials")

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True)
