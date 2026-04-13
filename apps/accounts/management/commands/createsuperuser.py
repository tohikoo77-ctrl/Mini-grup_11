from django.contrib.auth.management.commands.createsuperuser import Command as BaseCommand

class Command(BaseCommand):
    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument('--email', required=True)

    def handle(self, *args, **options):
        options['username'] = options['email']
        super().handle(*args, **options)
