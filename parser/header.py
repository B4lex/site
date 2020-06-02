import requests
from bs4 import BeautifulSoup


def get_image(link):
    # files_dir = r'/home/alex/Desktop/auto/'
    html_raw = requests.get(link)
    html_bs = BeautifulSoup(html_raw.content, 'html.parser')
    img_tag = html_bs.find('div', class_='photo-620x465')
    img_link = img_tag.find('img').get('src')
    img_file = requests.get(img_link)
    # with open(files_dir + 'auto.jpg', 'wb') as file:
    #     file.write(img_file.content)
    #     file.close()
    return img_file.content


def get_description(link):
    html_raw = requests.get(link)
    html_bs = BeautifulSoup(html_raw.content, 'html.parser')
    return html_bs.find('div', id='full-description').text.replace('//', '')
