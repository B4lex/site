import requests
from bs4 import BeautifulSoup
import os
from parsed_site.settings import BASE_DIR


def get_image(car_bs):
    # files_dir = r'/home/alex/Desktop/auto/'
    img_tag = car_bs.find('div', 'photo-620x465')
    if img_tag is None:
        return None
    img_link = img_tag.find('img').get('src')
    if img_link.endswith("s.jpg"):
        img_link = img_link.replace('s.jpg', 'f.jpg')
    # img_file = requests.get(img_link)
    # img_name = img_link[img_link.rfind('/') + 1:]
    # with open(os.path.join(BASE_DIR, 'cars_list/static/cars_list/cars_img/') + img_name, 'wb') as image:
    #     image.write(img_file.content)
    return img_link


def get_description(car_bs):
    block_params = car_bs.find(id='description_v3')
    if block_params is None:
        return []
    params = block_params.find_all('dd')
    text = ''
    for param in params:
        text += param.text + '\n'

    return text


def get_car_info(link):
    html_raw = requests.get(link)
    html_bs = BeautifulSoup(html_raw.content, 'html.parser')
    description = get_description(html_bs)
    image = get_image(html_bs)
    return {"description": description,
            "image": image}


def get_last_page_number(link):
    html_raw = requests.get(link)
    html_bs = BeautifulSoup(html_raw.content, 'html.parser')
    last_page = html_bs.findAll('span', class_='page-item mhide')[-1].find('a').text.replace(" ", "")
    return int(last_page)
