from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'List all superusers in the Django app'

    def handle(self, *args, **options):
        superusers = User.objects.filter(is_superuser=True)
        self.stdout.write("List of superusers:")
        for user in superusers:
            self.stdout.write(user.username)

