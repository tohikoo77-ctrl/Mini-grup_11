from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from apps.shared.models import BaseModel


class PaymentType(BaseModel, TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(
            verbose_name=_("Name"),
            max_length=20,
            unique=True,
            help_text=_("The name of the payment type"),
        ),
    )

    class Meta:
        ordering = ["created"]
        verbose_name = _("Payment Type")
        verbose_name_plural = _("Payment Types")

    def __str__(self):
        return self.safe_translation_getter("name", any_language=True)
