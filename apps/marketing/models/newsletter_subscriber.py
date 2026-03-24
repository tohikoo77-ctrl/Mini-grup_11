from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.shared.models import BaseModel


class NewsletterSubscriber(BaseModel):
    email = models.EmailField(
        verbose_name=_("Email"),
        unique=True,
    )

    consent = models.BooleanField(
        verbose_name=_("Consent"),
        default=False,
    )

    subscribed_at = models.DateTimeField(
        verbose_name=_("Subscribed At"),
        auto_now_add=True,
    )

    class Meta:
        ordering = ["-subscribed_at"]
        verbose_name = _("Newsletter Subscriber")
        verbose_name_plural = _("Newsletter Subscribers")

    def __str__(self):
        return self.email
