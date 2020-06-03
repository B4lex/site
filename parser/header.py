import requests
from bs4 import BeautifulSoup
import os
from parsed_site.settings import BASE_DIR


def get_image(link):
    # files_dir = r'/home/alex/Desktop/auto/'
    html_raw = requests.get(link)
    html_bs = BeautifulSoup(html_raw.content, 'html.parser')
    img_tag = html_bs.find('div', 'photo-620x465')
    if img_tag is None:
        return None
    img_link = img_tag.find('img').get('src')
    if 's.jpg' in img_link:
        img_link = img_link.replace('s.jpg', 'f.jpg')
    img_file = requests.get(img_link)
    img_name = img_link[img_link.rfind('/') + 1:]
    with open(os.path.join(BASE_DIR, 'cars_list/static/cars_list/cars_img/') + img_name, 'wb') as image:
        image.write(img_file.content)
    return img_name


def get_description(link):
    html_raw = requests.get(link)
    html_bs = BeautifulSoup(html_raw.content, 'html.parser')
    block_params = html_bs.find(id='description_v3')
    if block_params is None:
        return []
    params = block_params.find_all('dd')
    text = ''
    for param in params:
        text += param.text + '\n'

    return text


def get_pages(link):
    html_raw = requests.get(link)
    html_bs = BeautifulSoup(html_raw.content, 'html.parser')
    current_page = html_bs.findAll('span', class_='page-item mhide')[0].find('a').text
    last_page = html_bs.findAll('span', class_='page-item mhide')[-1].find('a').text
    return int(current_page), int(last_page)
