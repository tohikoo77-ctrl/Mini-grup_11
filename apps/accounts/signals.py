from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.accounts.models import Profile
from apps.notifications.models import NotificationSetting
from apps.payments.models import Wallet

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_related_objects(sender, instance, created, **kwargs):
    """
    Signal receiver to create a new Profile, SecuritySetting,
    NotificationSetting, and Wallet whenever a new User is created.
    """
    if created:
        # Create the profile first
        if not hasattr(instance, 'profile'):
            profile = Profile.objects.create(user=instance)
        else:
            profile = instance.profile

        # Then create the notification setting using the profile
        if not hasattr(profile, 'notification_setting'):
            NotificationSetting.objects.create(profile=profile)

        # Finally, create the wallet using the profile
        if not hasattr(profile, 'wallet'):
            Wallet.objects.create(profile=profile)