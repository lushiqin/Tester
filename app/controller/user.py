from django.shortcuts import HttpResponse,render
from app import models
import simplejson
import time

def addUser(request):
    responseBody = request.body
    responseData = simplejson.loads(responseBody.decode("utf-8"))
    data = {
        "userName":responseData['name'],
        "token":responseData['token'],
        "create_time":time.time(),
        "update_time":time.time()
    }
    try:
        models.user.objects.update_or_create(userPhone = responseData['phone'],defaults=data)
        print(models.user.objects.all())
    except Exception as e:
        print("-----------------------------------------")
        print(e)
        print("-----------------------------------------")
    return HttpResponse("200")


def secAll(request):
    userList = models.user.objects.all().values()
    users = []
    for i in userList:
        users.append(i)
    data = {
        "ret":1,
        "msg":"请求成功",
        "statusCode":200,
        "data":{
            "users":users
        }
    }
    return HttpResponse(simplejson.dumps(data))

def secOne(request):
    responseBody = request.body
    responseData = simplejson.loads(responseBody.decode('utf-8'))
    user = models.user.objects.get(userPhone=responseData['phone'])
    data = {
        "ret":1,
        "msg":"请求成功",
        "statusCode":200,
        "data":{
            "id":user.id,
            "userName":user.userName,
            "userPhone":user.userPhone,
            "token":user.token
        }
    }
    return HttpResponse(simplejson.dumps(data))