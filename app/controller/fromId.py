from django.shortcuts import HttpResponse,render
from app import models
import simplejson
import time
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import register_job,register_events,DjangoJobStore

def addFromId(request):
    print("访问到了addFromId")
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

schedulers = BackgroundScheduler()
@register_job(schedulers,"cron",day_of_week ='0-6',hour='00',minute='00',second='00',id="fromid_job")
def updFromid():
    print("跑定时任务updFromid",time.time())
    time7 = datetime.datetime.now()-datetime.timedelta(days=-6)
    inttime = int(time.mktime(time7.timetuple()))
    models.userFromId.objects.filter(create_time__gte=inttime).update(status =0,update_time=time.time())
try:
    schedulers.start()
except (KeyboardInterrupt,SystemExit):
    print("shutdown")
    schedulers.shutdown()