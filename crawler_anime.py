from bs4 import BeautifulSoup
import urllib.request

import requests

url =  'https://myanimelist.net/anime/16498/Shingeki_no_Kyojin'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

japanese_title = soup.find(class_ = 'title-name h1_bold_none').strong.get_text()
print(japanese_title)

english_title = soup.find(class_ = 'title-english title-inherit').get_text()
print(english_title)

score = soup.find(class_ = 'score-label score-8').get_text()
print(score)

tag = soup.find(class_ = 'fl-l score')
print(tag['data-user'].split()[0])