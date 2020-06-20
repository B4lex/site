from django.core.management.base import BaseCommand

from cars_list.parser import run

# base_url = 'https://auto.ria.com/legkovie/'
# start_page = 1


class Command(BaseCommand):

    def handle(self, *args, **options):
        run()
