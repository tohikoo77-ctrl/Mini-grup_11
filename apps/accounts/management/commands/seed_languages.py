from django.core.management.base import BaseCommand
import uuid

from apps.accounts.models import Language


class Command(BaseCommand):
    help = "Seed default languages"

    LANGUAGES = [
        ("en", "English (US)"),
        ("ru", "Russian"),
        ("uz", "Uzbek"),
        ("ar", "Arabic"),
        ("tg", "Tajik"),
        ("ja", "Japanese"),
    ]

    def handle(self, *args, **kwargs):
        for code, name in self.LANGUAGES:
            obj, created = Language.objects.get_or_create(
                code=code,
                defaults={"id": uuid.uuid4(), "name": name}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created language: {name} ({code})"))
            else:
                self.stdout.write(self.style.WARNING(f"Language already exists: {name} ({code})"))