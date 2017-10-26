from django.core.management.base import BaseCommand, CommandError
from shortner.models import KirrURL


class Command(BaseCommand):
    help = 'Refresh all KirrURL shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('items', type=int)

    def handle(self, *args, **kwargs):
        return KirrURL.objects.refresh_shortcodes(items=kwargs['items'])
