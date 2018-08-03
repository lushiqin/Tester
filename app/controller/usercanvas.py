from django.shortcuts import HttpResponse
from django.core import serializers
from app import models
import simplejson
import time

def insert(request):
    if request.method == 'POST':
        try:
            canvasimg = models.userCanvas(
                canvasImg = request.FILES.get('file'),
                moblie=request.POST['moblie'],
                canvasid = request.POST['canvasid'],
                answer = request.POST['answer'],
                create_time = time.time()
            )
            canvasimg.save()
        except Exception as e:
            print("error",e)
        return HttpResponse("200")
    else:
        return HttpResponse("400")

def select(request):
    if request.method == "POST":
        requestBody = request.body
        requestData = simplejson.loads(requestBody.decode('utf-8'))
        canvaslist = models.userCanvas.objects.filter(
            moblie=requestData['moblie'],
        canvasid=requestData['canvasid'] ).values()
        canvas = []
        for i in canvaslist:
            canvas.append(i)
        return HttpResponse(simplejson.dumps(canvas))

def basedata(request):
    if request.method =="POST":
        baselist = models.baseData.objects.filter().values()[:5]
        base = []
        for i in baselist:
            base.append(i)
        return HttpResponse(simplejson.dumps(base))