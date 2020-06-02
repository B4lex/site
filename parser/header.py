import requests
from bs4 import BeautifulSoup
import os
from parsed_site.settings import BASE_DIR


def get_image(link):
    # files_dir = r'/home/alex/Desktop/auto/'
    html_raw = requests.get(link)
    html_bs = BeautifulSoup(html_raw.content, 'html.parser')
    img_tag = html_bs.find('div', class_='photo-620x465')
    img_link = img_tag.find('img').get('src')
    img_file = requests.get(img_link)
    img_name = img_link[img_link.rfind('/') + 1:]
    with open(os.path.join(BASE_DIR, 'cars_list/static/cars_list/cars_img/') + img_name, 'wb') as image:
        image.write(img_file.content)
    return img_name


def get_description(link):
    html_raw = requests.get(link)
    html_bs = BeautifulSoup(html_raw.content, 'html.parser')
    return html_bs.find('div', id='full-description').text.replace('//', '')
