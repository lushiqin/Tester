from django.shortcuts import HttpResponse,render
from app import models
import requests
import simplejson
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
    responseBody = request.body
    content = json.loads(responseBody.decode('utf-8'))
    hostName = content['hostName']
    hostUrl = content['hostUrl']
    models.host.objects.create(hostName = hostName,hostUrl = hostUrl)
    return HttpResponse("200")


#查询所有服务器信息
def secHost(request):
    hostList = models.host.objects.all().values()
    hosts = []
    for i in hostList:
        hosts.append(i)
    return HttpResponse(simplejson.dumps(hosts))

#新增用户信息
def addUser(request):
    responseBody = request.body
    responseData = json.loads(responseBody.decode('utf-8'))
    models.user.objects.create(phone = responseData['phone'],name = responseData['name'],token=responseData['token'],status = responseData['status'])
    return HttpResponse("200")

#查询用户信息
def secUser(request):
    userList = models.user.objects.all().values()
    users = []
    for i in userList:
        users.append(i)
    return HttpResponse(simplejson.dumps(users))

#新增商品信息
def addCommo(request):
    responseBody = request.body
    responseData = json.loads(responseBody.decode('utf-8'))
    models.commodity.objects.create(commoName =responseData['commoName'],commoPrice = responseData['commoPrice'],commoInfo=responseData['commoInfo'],status=responseData['status'])
    return HttpResponse("200")

#查询商品信息
def secCommo(request):
    commoList = models.commodity.objects.all().values()
    commos = []
    for i in commos:
        commos.append(i)
    return HttpResponse(simplejson.dumps(commos))