from decimal import Decimal
import re

import requests
from bs4 import BeautifulSoup

HEADERS = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/83.0.4103.97 Safari/537.36'
}


def get_car_info(link):
    html_raw = requests.get(link, headers=HEADERS)
    html_bs = BeautifulSoup(html_raw.content, 'html.parser')
    stats = get_car_stats(html_bs)
    image = get_image(html_bs)
    location = get_location(html_bs)
    description = get_description(html_bs)
    info_dict = {'image_ref': image,
                 'location': location,
                 'description': description,
                 }
    info_dict.update(stats)
    return info_dict


def get_color(param):
    tag = param.find_all('span')[1]
    name = tag.text
    style = tag.find('span').get('style')
    color_val = style[style.find('#') + 1:style.find(';')]
    return name, color_val


def get_image(car_bs):
    img_tag = car_bs.find('div', class_='photo-620x465')
    if img_tag is None:
        img_tag = car_bs.find('div', class_='image-gallery-image')
    img_link = img_tag.find('img').get('src')
    if 'youtube' in img_link:
        img_tag = car_bs.find_all('a', class_='photo-74x56')[1]
        img_link = img_tag.find('img').get('src')
    if img_link.endswith("s.jpg"):
        img_link = img_link.replace('s.jpg', 'f.jpg')

    return img_link


def get_car_stats(car_bs):
    block_params = car_bs.find(id='description_v3')
    if block_params is None:
        return {}
    params = block_params.find_all('dd', class_='')
    stats = {'type': params[0].text}
    mileage = block_params.find('dd', class_='mhide').find_all('span')[1].text
    mileage_d = re.findall(r'\d+', mileage)
    if mileage_d:
        stats['mileage'] = Decimal(mileage_d[0])
    for param in params[1:]:
        span = param.find_all('span')
        title_field = span[0].text
        value_field = span[1].text
        if title_field == 'Двигатель':
            stats['engine'] = value_field
        elif title_field == 'Коробка передач':
            stats['gearbox'] = value_field
        elif title_field == 'Привод':
            stats['transmission'] = value_field
        elif title_field == 'Цвет':
            stats['color'], \
                stats['color_val'] = get_color(param)

    return stats


def get_location(car_bs):
    seller = car_bs.find('section', id='userInfoBlock')
    if seller:
        return seller.find('div', class_='item_inner').text
    seller = car_bs.find('section', class_='seller')
    if not seller:
        return None
    return seller.find('div', class_='item_inner').text


def get_description(car_bs):
    description = car_bs.find('div', id='full-description')
    if description:
        return description.text
    else:
        try:
            block = car_bs.find('h4', string='Комментарий автосалона').parent
            description = block.find('div')
        except AttributeError:
            return None
        return description.string


def get_last_page_number(link):
    html_raw = requests.get(link)
    html_bs = BeautifulSoup(html_raw.content, 'html.parser')
    last_page = html_bs.findAll('span', class_='page-item mhide')[-1].find('a').text.replace(" ", "")
    return int(last_page)
