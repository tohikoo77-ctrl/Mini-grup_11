from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from apps.shared.models import BaseModel


class Publication(BaseModel, TranslatableModel):
    cover = models.ImageField(
        verbose_name=_("Cover"),
        upload_to="publication_covers/",
        blank=True,
        null=True,
    )

    category = models.ForeignKey(
        to="content.PublicationCategory",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="publications",
        verbose_name=_("Category"),
    )

    published = models.BooleanField(
        verbose_name=_("Published"),
        default=False,
    )

    publication_date = models.DateField(
        verbose_name=_("Publication Date"),
        blank=True,
        null=True,
    )

    translations = TranslatedFields(
        title=models.CharField(
            verbose_name=_("Title"),
            max_length=255,
        ),
        body=models.TextField(
            verbose_name=_("Body"),
            blank=True,
            null=True,
        ),
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = _("Publication")
        verbose_name_plural = _("Publications")

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True)
