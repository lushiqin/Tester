from django.shortcuts import HttpResponse,render
from app import models

def addUser(request):
    return HttpResponse("200")


def secAll(request):
    print("1111")
    return HttpResponse("200")

def secOne(requset):
    return HttpResponse("200")