from django.shortcuts import HttpResponse,render
from app import models
import simplejson

def addUser(request):
    responseBody = request.body
    responseData = simplejson.loads(responseBody.decode("utf-8"))
    userPhone = responseData['phone']
    userToken = responseData['token']
    return HttpResponse("200")


def secAll(request):
    return HttpResponse("200")


def secOne(request):
    return HttpResponse("200")