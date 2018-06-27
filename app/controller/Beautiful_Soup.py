from bs4 import BeautifulSoup
from django.shortcuts import HttpResponse
import requests
import re
import simplejson

#获取首页 信息
def xs84(request):
    responseBody = request.body
    responseData = simplejson.loads(responseBody.decode('utf-8'))
    url = responseData['url']
    try:
        response = requests.get("http://www.xs84.la"+url)
        soup = BeautifulSoup(response.text,'lxml')
        navlist = soup.select('div .nav')[0].select("a")
        tupianList = soup.select('div #tupian')[0].select('li')
        newsList = soup.select('div .l')[0].select('li')
        newsputList = soup.select('div .r')[0].select('li')
        navs = []
        tups = []
        newrs = []
        newls = []
        data = {
            "nav":navs,
            "tup":tups,
            "newr":newrs,
            "newl":newls
        }
        for nav in navlist:
            navtag = {}
            navtag['url'] = nav['href']
            navtag['name'] = nav.string
            navs.append(navtag)
        for tup in tupianList:
            tuptag = {}
            tuptag['name'] = tup.h5.string
            tuptag['url']= tup.a['href']
            tups.append(tuptag)
        for newr in newsList:
            newrstag = {}
            newrr = newr.select('.s2')[0]
            newrstag['url'] = newrr.a['href']
            newrstag['name'] = newrr.a.string
            newrs.append(newrstag)
        for newl in newsputList:
            newlstag = {}
            newll = newl.select('.s2')[0]
            newlstag['url'] = newll.a['href']
            newlstag['name'] = newll.a.string
            newls.append(newlstag)
        return HttpResponse(simplejson.dumps(data))
    except Exception as e:
        return HttpResponse('无数据')
#获取小说目录
def xsml(request):
    response = requests.get("http://www.xs84.la/400962_0/")
    soup = BeautifulSoup(response.text,'lxml')
    try:
        mulu = soup.select("div #list")[0].select("a")
        mulus = []
        lists = {
            "ml":mulus
        }
        for i in mulu:
            mulutag = {}
            mulutag['url'] = i['href']
            mulutag['name'] = i.string
            mulus.append(mulutag)
        return HttpResponse(simplejson.dumps(lists))
    except Exception as e:
        return HttpResponse('无数据')
#获取章节信息
def xszj(request):
    responseBody = request.body
    responseData = simplejson.loads(responseBody.decode('utf-8'))
    url = responseData['url']
    print(url)
    try:
        response = requests.get("http://www.xs84.la"+url)
        soup = BeautifulSoup(response.text,'lxml')
        content = soup.select('div #content')
        return HttpResponse(content[0].encode('utf-8'))
    except Exception as e:
        return HttpResponse('无数据')