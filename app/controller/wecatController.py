from django.shortcuts import HttpResponse,render
from app import models
from threading import Timer
import time
import requests
import simplejson
import json

# POST方法
# responseBody = request.body
# responseData = simplejson.loads(responseBody.decode('utf-8'))
# 传给前端时，需要simplejson.dumps()
# GET方法
# responseBody = resquest.GET['name']
#解析请求结果内容时，


# 获取微信openid
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
