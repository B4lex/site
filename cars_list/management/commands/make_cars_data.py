from parser.header import *
from cars_list.models import Car
from django.core.management.base import BaseCommand


URL = 'https://auto.ria.com/legkovie/bmw/?page=1'


class Command(BaseCommand):

    def handle(self, *args, **options):
        raw_data = requests.get(URL)
        bs_data = BeautifulSoup(raw_data.content, 'html.parser')
        cars_raw = bs_data.find_all('section', class_='ticket-item new__ticket t paid')
        for car_raw in cars_raw:
            link = car_raw.find('a', class_='address').get('href')
            # car_fields = {
            #     'id': 0,
            #     'title': car_raw.find('span', class_='blue bold').text,
            #     'link': link,
            #     'image': get_image(link),
            #     'usd_price': car_raw.find('span', attrs={'data-currency': 'USD'}).text,
            #     'uah_price': car_raw.find('span', attrs={'data-currency': 'UAH'}).text,
            #     'description': get_description(link)
            # }
            car = Car()
            car.title = car_raw.find('span', class_='blue bold').text.strip(' ')
            car.link = link
            car.usd_price = int(car_raw.find('span', attrs={'data-currency': 'USD'}).text.replace(' ', ''))
            car.uah_price = int(car_raw.find('span', attrs={'data-currency': 'UAH'}).text.replace(' ', ''))
            car.description = get_description(link)
            car.image_ref = get_image(link)
            print(car.title + ' have successfully parsed.' + car.image_ref)
            car.save()

