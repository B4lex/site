from cars_list.models import Car
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import sys

import requests
from cars_list.parser import get_last_page_number, get_car_info

base_url = 'https://auto.ria.com/legkovie/'


class Command(BaseCommand):

    def handle(self, *args, **options):
        last_page = get_last_page_number(base_url)
        for page_number in range(1, last_page + 1):
            raw_data = requests.get(base_url, params={"page": page_number})
            bs_data = BeautifulSoup(raw_data.content, 'html.parser')
            cars_raw = bs_data.find_all('section', class_='ticket-item new__ticket t paid')
            for car_raw in cars_raw:
                link = car_raw.find('a', class_='address').get('href')
                print(link)
                defaults = {"title": car_raw.find('span', class_='blue bold').text.strip(' '),
                            "usd_price": int(
                                car_raw.find('span', attrs={'data-currency': 'USD'}).text.replace(' ', '')),
                            "uah_price": int(
                                car_raw.find('span', attrs={'data-currency': 'UAH'}).text.replace(' ', '')),
                            }
                defaults.update(get_car_info(link))
                obj, created = Car.objects.get_or_create(link=link,
                                                         defaults=defaults)
                if not created:
                    for item in defaults:
                        setattr(obj, item, defaults.get(item))
                        obj.save()

            print(str(page_number) + ' page have successfully parsed.')
            if page_number == 100:
                break
