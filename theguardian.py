from typing import Text
from bs4 import BeautifulSoup;
import requests
from csv import writer

query1='bangladesh';
query2=' '
operation='AND'
tag='politics';
fromDate='2014-01-01'
api='1997b4cf-fab9-4990-9a04-3e4722c6bd79'
url=f'https://content.guardianapis.com/search?q={query1}%20{operation}%20{query2}&tag={tag}/{tag}&from-date={fromDate}&api-key={api}'


page=requests.get(url).json()
# soup=BeautifulSoup(page.content,'html.parser')
# lists=soup.find_all('section',class_="listing-search-item")

with open('data.csv','w',encoding='utf8',newline='') as f:
  thewriter=writer(f)
  header=['Title','Section Name','Web Publication Date','Web Link']
  thewriter.writerow(header)
  for item in page['response']['results']:
    title=item["webTitle"]
    sectionName=item["sectionName"]
    webPublicationDate=item["webPublicationDate"]
    WebLink=item["webUrl"]
    info=[title,sectionName,webPublicationDate,WebLink]
    thewriter.writerow(info)
