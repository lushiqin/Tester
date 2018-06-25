from bs4 import BeautifulSoup
from django.shortcuts import HttpResponse
import requests
import re


def Test(request):
    try:
        response = requests.get("http://www.xs84.la/")
        soup = BeautifulSoup(response.text,'lxml')
        navlist = soup.select('div .nav')[0].select("a")
        tupianList = soup.select('div #tupian')[0].select('li')
        newsList = soup.select('div .l')[0].select('li')
        newsputList = soup.select('div .r')[0].select('li')
        print("导航：")
        for nav in navlist:
            print(nav['href'],nav.string)
        print("推荐小说：")
        for tup in tupianList:
            print(tup.a['href'],tup.h5.string)
        print("最近更新：")
        for newr in newsList:
            newrr = newr.select('.s2')[0]
            print(newrr.a['href'],newrr.a.string)
        print("最新入库：")
        for newl in newsputList:
            newll = newl.select('.s2')[0]
            print(newll.a['href'],newll.a.string)
        return HttpResponse(soup.prettify())
    except Exception as e:
        print(e)