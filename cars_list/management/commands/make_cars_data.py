from parser.header import *
from cars_list.models import Car
from django.core.management.base import BaseCommand


URL = 'https://auto.ria.com/legkovie/bmw/?page=1'


class Command(BaseCommand):

    def handle(self, *args, **options):
        Car.objects.all().delete()
        url = URL
        current_page, last_page = get_pages(url)
        while current_page <= last_page:
            raw_data = requests.get(url)
            bs_data = BeautifulSoup(raw_data.content, 'html.parser')
            cars_raw = bs_data.find_all('section', class_='ticket-item new__ticket t paid')
            for car_raw in cars_raw:
                link = car_raw.find('a', class_='address').get('href')
                car = Car()
                car.title = car_raw.find('span', class_='blue bold').text.strip(' ')
                car.link = link
                car.usd_price = int(car_raw.find('span', attrs={'data-currency': 'USD'}).text.replace(' ', ''))
                car.uah_price = int(car_raw.find('span', attrs={'data-currency': 'UAH'}).text.replace(' ', ''))
                car.image_ref = get_image(link)
                car.save()
            print(str(current_page) + ' page have successfully parsed.')
            url = bs_data.find('a', class_='page-link js-next').get('href')
            print(url)
            current_page += 1
