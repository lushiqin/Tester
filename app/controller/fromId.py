from django.shortcuts import HttpResponse,render
from app import models
import simplejson
import time

def addFromId(request):
    responseBody = request.body
    responseData = simplejson.loads(responseBody.decode("utf-8"))
    try:
        models.userFromId.objects.create(userId = responseData['userId'],
                                         userFromId = responseData['formId'],
                                         status = 1,
                                         create_time = time.time(),
                                         update_time = time.time())
        return HttpResponse("200")
    except Exception as e:
        return HttpResponse(e)


def secOne(request):
    return HttpResponse("200")