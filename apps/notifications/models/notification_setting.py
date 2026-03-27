from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.shared.models import BaseModel


class NotificationSetting(BaseModel):
    profile = models.ForeignKey(
        to="accounts.Profile",
        on_delete=models.CASCADE,
        related_name="notification_settings",
        verbose_name=_("Profile"),
        help_text=_("The profile this notification setting belongs to"),
    )
    general_notification = models.BooleanField(
        verbose_name=_("General Notification"),
        default=True,
    )
    sound = models.BooleanField(
        verbose_name=_("Sound"),
        default=True,
    )
    vibrate = models.BooleanField(
        verbose_name=_("Vibrate"),
        default=True,
    )
    special_offers = models.BooleanField(
        verbose_name=_("Special Offers"),
        default=True,
    )
    promo_and_discount = models.BooleanField(
        verbose_name=_("Promotions and Discounts"),
        default=True,
    )
    payments = models.BooleanField(
        verbose_name=_("Payments"),
        default=True,
    )
    cashback = models.BooleanField(
        verbose_name=_("Cashback"),
        default=True,
    )
    new_service_available = models.BooleanField(
        verbose_name=_("New Service Available"),
        default=True,
    )
    new_tips_available = models.BooleanField(
        verbose_name=_("New Tips Available"),
        default=True,
    )
    app_updates = models.BooleanField(
        verbose_name=_("App Updates"),
        default=True,
    )

    class Meta:
        verbose_name = _("Notification Setting")
        verbose_name_plural = _("Notification Settings")

    def __str__(self):
        return f"Notification settings for {self.profile}"
