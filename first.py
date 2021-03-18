#The second part of the code isn't working currently. But i'm in progress to fix this issue:)
#first part: getting html page
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
htmlpage = requests.get("https://rabota.by/search/vacancy?area=1002&fromSearchLine=true&st=searchVacancy&text=python&page=0", headers=headers)

soup = BeautifulSoup(htmlpage.text, 'html.parser')

#second part
def getLinks(url):
    html_page = urllib2.urlopen("https://rabota.by/search/vacancy?area=1002&fromSearchLine=true&st=searchVacancy&text=python&page=0", headers=headers)
    soup = BeautifulSoup(html_page)
    links = []

    for link in soup.findAll('a', attrs={'href': re.compile(f"query={'python'}$")}):
        links.append(link.get('href'))

print(links)
