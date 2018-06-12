from django.shortcuts import HttpResponse,render
from app import models
import simplejson
import time
import re


def addInterface(request):
    responseBody = request.body
    responseData = simplejson.loads(responseBody.decode("utf-8"))
    data = responseData['data']
    pattern = re.compile(r'\w+')
    models.interfaceInfo.objects.create( interfaceName = responseData['interfaceName'],
                                         interfaceUrl = responseData['interfaceUrl'],
                                         methodType = responseData['methodType'],
                                         data = pattern.findall(data),
                                         status =1,
                                         create_time=time.time(),update_time=time.time())
    return HttpResponse("200")


def secAll(request):
    interfaceList = models.interfaceInfo.objects.all().values()
    interfaces = []
    for i in interfaceList:
        #获取data字符串
        strData = i['data']
        #将data字符串转换为list
        listData = simplejson.loads(str.replace(strData,"'",'"'))
        i['data'] = listData
        interfaces.append(i)
    return HttpResponse(simplejson.dumps(interfaces))


def secOne(request):
    responseBody = request.body
    responseData = simplejson.loads(responseBody.decode('utf-8'))
    print(responseData)
    return HttpResponse(responseData)