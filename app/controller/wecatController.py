from django.shortcuts import HttpResponse,render
from app import models

def getOpenId(request):
    return HttpResponse("请求成功")