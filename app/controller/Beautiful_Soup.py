from bs4 import BeautifulSoup
from django.shortcuts import HttpResponse
import requests
import simplejson
import time

#获取首页 信息
def xs84(request):
    responseBody  = request.body
    responseData = simplejson.loads(responseBody.decode("utf-8"))
    content = responseData['content']
    navs = []
    tups = []
    newrs = []
    newls = []
    data = {
        "nav": navs,
        "tup": tups,
        "newr": newrs,
        "newl": newls
    }
    try:
        soup = BeautifulSoup(content, 'lxml')
        try:
            navlist = soup.select('div .nav')[0].select("a")
            for nav in navlist:
                navtag = {}
                navtag['url'] = nav['href']
                navtag['name'] = nav.string
                navs.append(navtag)
        except Exception as e:
            print("navlist--",e)
        try:
            tupianList = soup.select('div #tupian')[0].select('li')
            for tup in tupianList:
                tuptag = {}
                tuptag['name'] = tup.h5.string
                tuptag['url'] = tup.a['href']
                tuptag['imgurl'] = tup.img['src']
                tups.append(tuptag)
        except Exception as e:
            print("tuplist--",e)
        try:
            newsList = soup.select('#newscontent')[0].select('li')
            for newr in newsList:
                newrstag = {}
                newrstag['url'] = newr.a['href']
                newrstag['name'] = newr.a.string
                newrs.append(newrstag)
        except Exception as e:
            print("newslist---",e)
        try:
            print("++++++++")
            newsputList = soup.select('#newscontent')[1].select('li')
            print("---======",newsputList)
            for newl in newsputList:
                newlstag = {}
                newlstag['url'] = newl.a['href']
                newlstag['name'] = newl.a.string
                newls.append(newlstag)
        except Exception as e:
            print("newsputList-2323232323-",e)
        return HttpResponse(simplejson.dumps(data))
    except Exception as e:
        print("出错了",e)
        return HttpResponse(e)
#获取小说目录
def xsml(request):
    responseBody  = request.body
    responseData = simplejson.loads(responseBody.decode("utf-8"))
    content = responseData['content']
    soup = BeautifulSoup(content,'lxml')
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

def xstest(request):
    responseBody  = request.body
    responseData = simplejson.loads(responseBody.decode("utf-8"))
    content = responseData['content']
    soup  = BeautifulSoup(content,'lxml')
    navlist = soup.select('div #tupian')[0].select('li')
    return HttpResponse(navlist)