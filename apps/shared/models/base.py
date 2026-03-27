from django.db import models
import uuid
from django.utils import timezone


class BaseModel(models.Model):
    """
    Abstract base model with UUID PK, timestamps, and common utilities.
    All models should inherit from this class.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="Timestamp when the object was created",
    )
    modified = models.DateTimeField(
        auto_now=True,
        verbose_name="Modified At",
        help_text="Timestamp when the object was last modified",
    )

    class Meta:
        abstract = True
        ordering = ["-created"]  # Default ordering: newest first
        get_latest_by = "created"

    def __str__(self):
        """
        Returns a string representation.
        If the model has a 'name' or 'title' attribute, return it, else UUID.
        """
        for attr in ["name", "title", "full_name"]:
            if hasattr(self, attr):
                value = getattr(self, attr)
                if value:
                    return str(value)
        return str(self.id)

    def save(self, *args, **kwargs):
        """
        Can be overridden in child models for custom pre-save behavior.
        """
        super().save(*args, **kwargs)

    @property
    def age_seconds(self):
        """
        Returns the age of the object in seconds since creation.
        """
        return (timezone.now() - self.created).total_seconds()
