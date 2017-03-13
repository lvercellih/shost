from django.core.management.base import BaseCommand

from shost import setup


class Command(BaseCommand):
    help = 'Setup the app'

    def handle(self, *args, **options):
        self.stdout.write('Starting setup...')
        setup.setup()
        self.stdout.write(self.style.SUCCESS('Setup successful!'))
