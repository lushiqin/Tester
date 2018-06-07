from django.shortcuts import HttpResponse,render
from app import models
import requests
import simplejson
import time

#获取微信openid
def getOpenId(request):
    response = request.body
    postData = simplejson.loads(response.decode('utf-8'))
    code = postData['code']
    url = "https://api.weixin.qq.com/sns/jscode2session"
    param = {
        "appid":"wx9fd2a84766c0dda5",
        "secret":"e106036d80c977244519f4f1753223dc",
        "js_code":code,
        "grant_type":"authorization_code"
    }
    response = requests.get(url=url,params=param)
    return HttpResponse(response.text)

#获取发送消息需要的accesstoken，有效时长为7200
def GetAccesstoken(msg,starttime):
    url = "https://api.weixin.qq.com/cgi-bin/token"
    data = {
        "grant_type":"client_credential",
        "appid":"wx9fd2a84766c0dda5",
        "secret":"e106036d80c977244519f4f1753223dc",
    }
    response = requests.get(url=url,params=data)
    cont = simplejson.loads(response.text)
    models.accessToken.objects.update(access_token = cont['access_token'],updatetime = time.time())
