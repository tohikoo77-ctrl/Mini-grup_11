from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from apps.shared.models import BaseModel
from apps.shared.enums import DiscountTypes
from .promotion_category import PromotionCategory


class Promotion(BaseModel, TranslatableModel):
    code = models.CharField(
        verbose_name=_("Code"),
        max_length=20,
        unique=True,
        blank=True,
        null=True,
        help_text=_("The unique code for the promotion"),
    )
    category = models.ForeignKey(
        PromotionCategory,
        on_delete=models.CASCADE,
        related_name="promotions",
        verbose_name=_("Category"),
        help_text=_("The category this promotion belongs to"),
    )
    discount_type = models.CharField(
        verbose_name=_("Discount Type"),
        max_length=10,
        choices=DiscountTypes.choices,
        default=DiscountTypes.PERCENT,
        help_text=_("The type of discount applied"),
    )
    discount_value = models.IntegerField(
        verbose_name=_("Discount Value"),
        help_text=_("The value of the discount"),
    )
    valid_from = models.DateTimeField(
        verbose_name=_("Valid From"),
        blank=True,
        null=True,
        help_text=_("The start date of the promotion"),
    )
    valid_to = models.DateTimeField(
        verbose_name=_("Valid To"),
        blank=True,
        null=True,
        help_text=_("The expiry date of the promotion"),
    )
    minimum_spend = models.IntegerField(
        verbose_name=_("Minimum Spend"),
        blank=True,
        null=True,
        help_text=_("Minimum spend required to apply this promotion"),
    )
    usage_limit = models.SmallIntegerField(
        verbose_name=_("Usage Limit"),
        blank=True,
        null=True,
        help_text=_("Maximum number of times this promotion can be used"),
    )
    used_count = models.SmallIntegerField(
        verbose_name=_("Used Count"),
        default=0,
        help_text=_("Number of times the promotion has been used"),
    )
    is_featured = models.BooleanField(
        verbose_name=_("Is Featured"),
        default=False,
        help_text=_("Whether this promotion should be featured prominently"),
    )
    display_order = models.SmallIntegerField(
        verbose_name=_("Display Order"),
        default=1,
        help_text=_("Order in which the promotion is displayed"),
    )

    translations = TranslatedFields(
        title=models.CharField(
            verbose_name=_("Title"),
            max_length=100,
            help_text=_("The title of the promotion"),
        ),
        subtitle=models.CharField(
            verbose_name=_("Subtitle"),
            max_length=200,
            blank=True,
            null=True,
            help_text=_("Optional subtitle for additional context"),
        ),
        description=models.TextField(
            verbose_name=_("Description"),
            blank=True,
            null=True,
            help_text=_("Optional description of the promotion"),
        ),
        terms_conditions=models.TextField(
            verbose_name=_("Terms & Conditions"),
            blank=True,
            null=True,
            help_text=_("Terms and conditions for the promotion"),
        ),
    )

    class Meta:
        ordering = ["display_order", "-created"]
        verbose_name = _("Promotion")
        verbose_name_plural = _("Promotions")

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True)

    @property
    def is_active(self):
        """Check if promotion is currently active"""
        from django.utils import timezone
        now = timezone.now()

        if self.valid_from and now < self.valid_from:
            return False
        if self.valid_to and now > self.valid_to:
            return False
        if self.usage_limit and self.used_count >= self.usage_limit:
            return False

        return True

    @property
    def discount_display(self):
        """Format discount for display"""
        if self.discount_type == DiscountTypes.PERCENT:
            return f"{self.discount_value}%"
        else:
            return f"${self.discount_value}"