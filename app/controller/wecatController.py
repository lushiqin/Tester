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

#定时更新accesstoken
def TimerAccesstoken(msg,starttime):
    url = "https://api.weixin.qq.com/cgi-bin/token"
    data = {
        "grant_type":"client_credential",
        "appid":"wx9fd2a84766c0dda5",
        "secret":"e106036d80c977244519f4f1753223dc",
    }
    response = requests.get(url=url,params=data)
    cont = simplejson.loads(response.text)
    models.AccessToken.objects.update(access_token = cont['access_token'],updatetime = time.time())


#新增服务器信息
def addHost(request):
    responseBody = request.body
    content = json.loads(responseBody.decode('utf-8'))
    data = {
        "hostName":content['hostName'],
        "hostUrl":content['hostUrl']
    }
    models.host.objects.update_or_create(hostUrl = content['hostUrl'],defaults=data)
    return HttpResponse("200")


#查询所有服务器信息
def secHost(request):
    hostList = models.host.objects.all().values()
    hosts = []
    for i in hostList:
        hosts.append(i)
    return HttpResponse(simplejson.dumps(hosts))
# 保存接口数据
def addInter(request):
    responseBody=request.body
    responseData = json.loads(responseBody.decode('utf-8'))
    data = {
        "nameUrl":responseData['interName'],
        "addressUrl":responseData['interUrl']
    }
    try:
        models.interfaceUrl.objects.update_or_create(addressUrl=responseData['interUrl'],defaults=data)
    except Exception as e:
        print(e)
    return HttpResponse("200")
# 查询接口信息
def secInter(request):
    interList = models.interfaceUrl.objects.all().values()
    inters = []
    for i in interList:
        inters.append(i)
    return HttpResponse(simplejson.dumps(inters))

#新增用户信息
def addUser(request):
    responseBody = request.body
    responseData = json.loads(responseBody.decode('utf-8'))
    data={
        "name":responseData["name"],
        "phone":responseData["phone"],
        "token":responseData["token"],
        "openid":responseData["openid"],
        "session_key":responseData["session_key"],
        "status":responseData["status"]
    }
    try:
        models.user.objects.update_or_create(phone = responseData['phone'],defaults=data)
    except Exception as e:
        print(e)
    return HttpResponse("200")

#查询用户信息
def secUser(request):
    userList = models.user.objects.all().values()
    users = []
    for i in userList:
        users.append(i)
    return HttpResponse(simplejson.dumps(users))
def secOneUser(request):
    responseBody = request.body
    responseData =json.loads(responseBody.decode('utf-8'))
    try:
        user = models.user.objects.get(phone = responseData['phone'])
        return HttpResponse(simplejson.dumps(user))
    except Exception as e:
        return HttpResponse("无数据")

#新增商品信息
def addCommo(request):
    responseBody = request.body
    responseData = json.loads(responseBody.decode('utf-8'))
    data = {
        "commoName":responseData['commoName'],
        "commoPrice": responseData['commoPrice'],
        "commoInfo": responseData['commoInfo'],
        "status": responseData['status'],
    }
    models.commodity.objects.update_or_create(commoName = responseData['commoName'],defaults=data)
    return HttpResponse("200")

#查询商品信息
def secCommo(request):
    commoList = models.commodity.objects.all().values()
    commos = []
    for i in commos:
        commos.append(i)
    return HttpResponse(simplejson.dumps(commos))

#存储用户formID
def saveUserFormId(request):
    responseBody = request.body
    responseData = json.loads(responseBody.decode('utf-8'))
    data = {
        "userId":responseData['userId'],
        "fromId":responseData['fromId'],
        "status":1,
        "creattime":time.time(),
        "updatetime":time.time()
    }
    models.userFromId.objects.update_or_create(fromId =responseData['fromId'],defaults=data)
    return HttpResponse("200")
