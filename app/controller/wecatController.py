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


# def postTest(requset):
#     postData = requset.body
#     postData1 = postData.decode('utf-8')
#     postData2 = json.loads(postData1)
#     print("loads = ",postData2)
#     try:
#         # print("no loads = ",postData1['username'])
#         print("loads = ",postData2['username'])
#     except Exception as e:
#         print(e)
#     return HttpResponse("11111")