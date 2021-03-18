
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
htmlpage = requests.get("https://rabota.by/search/vacancy?area=1002&fromSearchLine=true&st=searchVacancy&text=python&page=0", headers=headers)

soup = BeautifulSoup(htmlpage.text, 'html.parser')

print(soup)
