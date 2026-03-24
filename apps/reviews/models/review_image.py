from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.shared.models import BaseModel


class ReviewImage(BaseModel):
    review = models.ForeignKey(
        to="reviews.Review",
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name=_("Review"),
    )

    photo = models.ImageField(
        verbose_name=_("Photo"),
        upload_to="review_images/",
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = _("Review Image")
        verbose_name_plural = _("Review Images")

    def __str__(self):
        return f"Image for {self.review}"
