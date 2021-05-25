from bs4 import BeautifulSoup
import urllib.request
import requests

import csv

url =  'https://myanimelist.net/topanime.php?limit=0'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

ranking_list = soup.find_all(class_ = 'ranking-list')

with open('hot.csv', 'w', newline='', encoding='utf-8') as file:
    fieldnames = ['title', 'info', 'score', 'image']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    for item in ranking_list:
        img = item.find('a', class_ = 'hoverinfo_trigger fl-l ml12 mr8').img['data-src']
        title = item.find(class_='hoverinfo_trigger fl-l fs14 fw-b anime_ranking_h3').get_text()
        info = item.find(class_='information di-ib mt4').get_text()
        score = item.find('div', class_='js-top-ranking-score-col di-ib al').span.get_text()

        writer.writerow({'title': title, 'info': info, 'score': score, 'image': img})
        
    file.close()