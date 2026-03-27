from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.shared.models import BaseModel


class Language(BaseModel):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=100,
        unique=True,
        help_text=_("The name of the language"),
    )
    code = models.CharField(
        verbose_name=_("Code"),
        max_length=50,
        unique=True,
        default="english_us",
        help_text=_("The language code, e.g., 'english_us'"),
    )

    class Meta:
        ordering = ["created"]
        verbose_name = _("Language")
        verbose_name_plural = _("Languages")

    def __str__(self):
        return self.name
