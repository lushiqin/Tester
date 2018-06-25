from django.shortcuts import HttpResponse,render
from app import models
import requests
import simplejson
import time
from app.controller import accessToken
from app.controller import fromId
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


#发送模版消息
def setmessage(request):
    responseBody = request.body
    responseData = simplejson.loads(responseBody.decode('utf-8'))
    try:
        userFromId = fromId.secOne(responseData['openid'])['userFromId']
        access_token = accessToken.saveDb()
        openId = responseData['openid']
        templateId = "snFhkAziKZninEfFzEQAajBCUsCt6G5JVYt9986I5UA"
        interurl = responseData['k1']
        intersend = str(responseData['k2'])
        interData = str(responseData['k3'])
        interTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        interCode = responseData['k5']
        if(len(interData)>200):
            interData = interData[0:100]
        if(len(intersend)>200):
            intersend = intersend[0:100]
        url = "https://api.weixin.qq.com/cgi-bin/message/wxopen/template/send?access_token="+access_token
        content = {
            "touser": openId,
            "template_id": templateId,
            "form_id": userFromId,
            "data": {
                "keyword1": {
                    "value": interurl,
                    "color": "#173177"
                },
                "keyword2": {
                    "value": intersend,
                    "color": "#173177"
                },
                "keyword3": {
                    "value": interData,
                    "color": "#173177"
                },
                "keyword4": {
                    "value": interTime,
                    "color": "#173177"
                },
                "keyword5": {
                    "value": str(interCode),
                    "color": "#173177"
                }
            },
            "emphasis_keyword": "keyword1.DATA"
        }
        response = requests.post(url=url,data=simplejson.dumps(content)).json()
        if(response['errcode'] == 0):
            models.userFromId.objects.filter(userFromId=userFromId).update(status = 0)
        elif(response['errcode'] ==41028):
            print("form_id不正确，或者过期")
        elif (response['errcode'] == 41029):
            print("form_id已被使用")
        elif (response['errcode'] == 45009):
            print("接口调用超过限额（目前默认每个帐号日调用限额为100万）")
        else:
            print(response)

    except Exception as e:
        print("error",e)
    return HttpResponse("200")
