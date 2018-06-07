from django.shortcuts import HttpResponse,render
from app import models
import requests
import simplejson
import time


#获取发送消息需要的accesstoken并保存，有效时长为7200
def saveDb(msg,starttime):
    url = "https://api.weixin.qq.com/cgi-bin/token"
    data = {
        "grant_type":"client_credential",
        "appid":"wx9fd2a84766c0dda5",
        "secret":"e106036d80c977244519f4f1753223dc",
    }
    response = requests.get(url=url,params=data)
    cont = simplejson.loads(response.text)
    models.accessToken.objects.update(access_token = cont['access_token'],updatetime = time.time())


#更新accesstoken信息
def updateDb(request):
    HttpResponse("200")