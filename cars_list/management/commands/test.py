from cars_list.models import Car
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup

import requests
from cars_list.parser import get_image


class Command(BaseCommand):

    def handle(self, *args, **options):
        link = 'https://auto.ria.com/newauto/auto-mercedes-benz-gls-class-1834159.html'
        html_raw = requests.get(link)
        html_bs = BeautifulSoup(html_raw.content, 'html.parser')
        result = get_image(html_bs)
        print(result)
