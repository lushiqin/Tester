from django.shortcuts import HttpResponse,render
from app import models
import simplejson
import time

def addFromId(request):
    responseBody = request.body
    responseData = simplejson.loads(responseBody.decode("utf-8"))
    if(responseData['formId'] == "the formId is a mock one"):
        return HttpResponse("模拟器不保存")
    else:
        try:
            models.userFromId.objects.create(openId = responseData['openId'],
                                             userFromId = responseData['formId'],
                                             status = 1,
                                             create_time = time.time(),
                                             update_time = time.time())
            return HttpResponse("200")
        except Exception as e:
            return HttpResponse(e)


def secOne(openId):
    result = models.userFromId.objects.filter(status=1, openId=openId ).values()[0]
    return result