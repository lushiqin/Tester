from django.shortcuts import HttpResponse,render
from app import models
import simplejson

def addHost(request):
    return HttpResponse("200")



def secAll(request):
    hostList = models.hostInfo.objects.all().values()
    hosts = []
    for i in hostList:
        hosts.append(i)
    return HttpResponse(simplejson.dumps(hosts))

def secOne(request):
    return HttpResponse("200")