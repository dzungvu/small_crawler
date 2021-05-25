from bs4 import BeautifulSoup
import requests

import csv

url =  'https://www.netflix.com/vn-en/browse/genre/6721'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

ranking_list = soup.find_all(class_ = 'nm-collections-row')

with open('nexflix_anime.csv', 'w', newline='', encoding='utf-8') as file:
    fieldnames = ['group', 'title', 'image', 'detail_url']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    for item in ranking_list:
        group = item.find('h2', class_='nm-collections-row-name').get_text()

        list_small_item = item.find_all(class_='nm-content-horizontal-row-item')
        for small_item in list_small_item:

            title = small_item.find('span', class_='nm-collections-title-name').get_text()

            detail_url = ''
            detail_urls = small_item.find_all('a', href = True)
            for url in detail_urls:
                detail_url = url['href']
                img = url.img['src']

            writer.writerow({'group': group, 'title': title, 'image': img, 'detail_url': detail_url})
        
    file.close()