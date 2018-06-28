from django.shortcuts import HttpResponse
import requests
from bs4 import BeautifulSoup
import simplejson

# http://www.biquge.com.tw/

def homePage(request):
    navs = []
    hots = []
    spush = []
    novels = []
    news = []
    data = {
        "nav": navs,
        "hots": hots,
        "spush": spush,
        "novels": novels,
        "news":news,
    }
    try:
        responseBody = request.body
        responseData = simplejson.loads(responseBody.decode("utf-8"))
        responseUrl = responseData['url']
        responseC = requests.get("http://www.biquge.com.tw"+responseUrl).content
        #使用BeautifulSoup
        soup = BeautifulSoup(responseC,"lxml")
        #获取导航信息
        navList = soup.select(".nav")[0].select("a")
        #将导航name和URL存入list
        for i in navList:
            nav = {}
            nav['name'] = i.string
            nav['url'] = i['href']
            navs.append(nav)
        #获取热门小说信息
        hotbookList = soup.select("#hotcontent")[0].select(".item")
        for i in hotbookList:
            hot = {}
            hot['name'] = i.select("dt")[0].find("a").string
            hot['url'] = i.select("dt")[0].find("a")['href']
            hots.append(hot)

        #获取上期强推
        try:
            strongPushList = soup.select("#hotcontent")[0].select(".r")[0].select("ul")[1].select("li")
            for i in strongPushList:
                push = {}
                push['name'] = i.select("a")[0].string
                push['url'] = i.select("a")[0]['href']
                spush.append(push)
        except Exception as e:
            spush = []

        #获取类型推荐小说
        try:
            typenovels = soup.select(".novelslist")
            for i in typenovels:
                content = i.select("a")
                for j in content:
                    novel = {}
                    novel['name'] = j.string
                    novel['url'] = j['href']
                    novels.append(novel)
        except Exception as e:
            novels = []

        #获取最近更新和新入库小说
        newupdList = soup.select("#newscontent")[0].select(".s2")
        for i in newupdList:
            new = {}
            new['name'] = i.a.string
            new['url'] = i.a['href']
            news.append(new)
        return HttpResponse(simplejson.dumps(data))
    except Exception as e:
        print(e)
        return HttpResponse("粗错啦")

def catalog(request):
    mulus = []
    lists = {
        "ml": mulus
    }
    try:
        responseBody = request.body
        responseData = simplejson.loads(responseBody.decode("utf-8"))
        responseUrl = responseData['url']
        response = requests.get(responseUrl).content
        soup = BeautifulSoup(response,'lxml')
        catalogList = soup.select("#list")[0].select("a")
        for i in catalogList:
            cata = {}
            cata['name'] = i.string
            cata['url'] = i['href']
            mulus.append(cata)
    except Exception as e:
        print(e)
    return HttpResponse(simplejson.dumps(lists))

def details(request):
    lastchapter = ""
    nextchapter = ""
    contentbody = ""
    try:
        responseBody = request.body
        responseData = simplejson.loads(responseBody.decode('utf-8'))
        responseUrl = responseData['url']
        response = requests.get("http://www.biquge.com.tw"+responseUrl).content
        soup = BeautifulSoup(response,'lxml')
        chapname = soup.select(".bookname")[0].select("h1")[0].string
        lastchapter = soup.select(".bottem1")[0].select("a")[1]['href']
        nextchapter = soup.select(".bottem1")[0].select("a")[3]['href']
        contentbody = soup.select("#content")[0].encode("utf-8")
        data = {
            "chapname":chapname,
            "lastchapter": lastchapter,
            "nextchapter": nextchapter,
            "contentbody": contentbody
        }
        return HttpResponse(simplejson.dumps(data))
    except Exception as e:
        print(e)