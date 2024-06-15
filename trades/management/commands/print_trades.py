from django.core.management.base import BaseCommand
from trades.models import Trade

class Command(BaseCommand):
    help = 'Prints all trade records'

    def handle(self, *args, **kwargs):
        trades = Trade.objects.all()
        for trade in trades:
            self.stdout.write(f'{trade}')
