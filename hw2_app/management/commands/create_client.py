from django.core.management.base import BaseCommand
from hw2_app.models import Client


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        client = Client(name='Egor', email='egor@example.com', phone='9117776655', address='Lenina 1')
        client.save()
        self.stdout.write(f'{client}')