from typing import Text
from bs4 import BeautifulSoup;
import requests
from csv import writer
url="https://www.pararius.com/apartments/amsterdam?ac=1"
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')
lists=soup.find_all('section',class_="listing-search-item")

with open('housing.csv','w',encoding='utf8',newline='') as f:
  thewriter=writer(f)
  header=['Title','Location','Price','Area']
  thewriter.writerow(header)
  for item in lists:
    title=item.find("a",class_="listing-search-item__link--title").text.replace('\n','').strip();
    location=item.find("div",class_="listing-search-item__sub-title").text.replace('\n','').strip();
    price=item.find("div",class_="listing-search-item__price").text.replace('\n','').strip();
    area=item.find("li",class_="illustrated-features__item").text.replace('\n','').strip();
    price=price[1:]
    area=area[:len(area)-2]+'meter square'
    info=[title,location,price,area]
    thewriter.writerow(info)
