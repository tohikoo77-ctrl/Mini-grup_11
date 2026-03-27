from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from apps.shared.models import BaseModel


class Notification(BaseModel, TranslatableModel):
    icon = models.BinaryField(
        verbose_name=_("Icon"),
        help_text=_("The icon associated with the notification"),
    )

    translations = TranslatedFields(
        title=models.CharField(
            verbose_name=_("Title"),
            max_length=255,
            help_text=_("The title of the notification"),
        ),
        description=models.TextField(
            verbose_name=_("Description"),
            help_text=_("The description or body of the notification"),
        ),
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = _("Notification")
        verbose_name_plural = _("Notifications")

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True)
