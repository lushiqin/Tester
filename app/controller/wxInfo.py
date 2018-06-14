from django.shortcuts import HttpResponse,render
from app import models
import requests
import simplejson
import time
from app.controller import accessToken

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
        formId = models.userFromId.objects.filter(
            status=1,userId=responseData['userId']).values()[0]
        access_token = accessToken.saveDb()
        openId = responseData['openid']
        templateId = "snFhkAziKZninEfFzEQAajBCUsCt6G5JVYt9986I5UA"
        formIds = formId['userFromId']
        key1 = responseData['k1']
        key2 = responseData['k2']
        key3 = responseData['k3']
        key4 = time.time()
        key5 = responseData['k5']
        url = "https://api.weixin.qq.com/cgi-bin/message/wxopen/template/send?access_token="+access_token

        content = {
            "touser": openId,
            "template_id": templateId,
            "form_id": formIds,
            "data": {
                "keyword1": {
                    "value": key1,
                    "color": "#173177"
                },
                "keyword2": {
                    "value": key2,
                    "color": "#173177"
                },
                "keyword3": {
                    "value": key3,
                    "color": "#173177"
                },
                "keyword4": {
                    "value": key4,
                    "color": "#173177"
                },
                "keyword5": {
                    "value": key5,
                    "color": "#173177"
                }
            },
            "emphasis_keyword": "keyword1.DATA"
        }
        response = requests.post(url=url,data=simplejson.dumps(content)).json()
        if(response['errcode'] == 0):
            models.userFromId.objects.filter(userFromId=formIds).update(status = 0)

    except Exception as e:
        print("error",e)
    return HttpResponse("200")
