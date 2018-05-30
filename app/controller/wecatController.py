from django.shortcuts import HttpResponse,render
from app import models
import requests
import json
# 获取微信openid
def getOpenId(request):
    response = request.body
    postData = json.loads(response.decode('utf-8'))
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

#新增服务器信息
def addHost(request):
    hostName = ""
    hostUrl = ""
    models.host.objects.create(hostName = hostName,hostUrl = hostUrl)
    return HttpResponse("addhost")
#查询所有服务器信息
def secHost(request):
    hostList = models.host.objects.all()
    return HttpResponse(hostList)