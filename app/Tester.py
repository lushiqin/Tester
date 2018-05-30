from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse

def createUser(request):
    return HttpResponse("请求成功")

def createHost(request):
    return HttpResponse("请求成功")

def createUrl(request):
    return HttpResponse("请求成功")