from django.shortcuts import render

# Create your views here.
import requests
from bs4 import BeautifulSoup

toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'html5lib')

toi_headings = toi_soup.find_all('h2')

toi_headings = toi_headings[0:-13] # removing footer link

toi_news = []

for th in toi_headings:
    toi_news.append(th.text)

#getting news from hindustan times 
    
ht_r = requests.get("https://www.hindustantimes.com/india-news/")
ht_soup = BeautifulSoup(ht_r.content,'html5lib')
ht_headings = ht_soup.findAll("div", {"class": "headingfour"})
ht_headings = ht_headings[2:]
ht_news = []

for hth in ht_headings:
    ht_news.append(hth.text)


def index(req):
    
    return render(req, 'news/index.html',{'toi_news':toi_news,'ht_news':ht_news})