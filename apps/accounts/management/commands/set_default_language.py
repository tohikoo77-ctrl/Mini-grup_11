from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import transaction

from apps.accounts.models import Language, Profile


class Command(BaseCommand):
    help = "Ensure all users have profiles and set English as default app language"

    def add_arguments(self, parser):
        parser.add_argument(
            "--force",
            action="store_true",
            help="Override existing languages (set all to English)",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        User = get_user_model()
        force = options["force"]

        try:
            english = Language.objects.get(code="en")
        except Language.DoesNotExist:
            self.stdout.write(self.style.ERROR("English language (code='en') not found"))
            return

        # 1. Create missing profiles
        users_without_profile = User.objects.filter(profile__isnull=True)
        profiles_to_create = [
            Profile(user=user, app_language=english)
            for user in users_without_profile
        ]
        Profile.objects.bulk_create(profiles_to_create, batch_size=1000)

        created_count = len(profiles_to_create)

        # 2. Update existing profiles
        if force:
            updated_count = Profile.objects.exclude(app_language=english).update(app_language=english)
        else:
            updated_count = Profile.objects.filter(app_language__isnull=True).update(app_language=english)

        # 3. Output summary
        self.stdout.write(
            self.style.SUCCESS(
                f"Profiles created: {created_count}, Profiles updated: {updated_count}"
            )
        )
