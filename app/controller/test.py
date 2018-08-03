from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore,register_events,register_job
import time
import requests

schedulers = BackgroundScheduler()
@register_job(schedulers,"interval",seconds=60)
def test():
    print("hello world ")

def Test_login():
    print("登陆接口")
schedulers.start()
