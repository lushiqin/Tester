from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from app.models import host

def Tester(request):
    #查询
    selectValue = host.objects.get(id = 1).hostName.encode("utf-8")
    #修改
    host.objects.filter(id = 1).update(hostName = "我的服务器")
    #增加
    host.objects.create(hostName = "我的服务器咯",hostUrl = "www.baidu.com")
    #删除
    host.objects.filter(id = 2).delete()

    return HttpResponse(selectValue)