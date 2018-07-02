from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore,register_events,register_job
import time

schedulers = BackgroundScheduler()
@register_job(schedulers,"interval",seconds=600)
def test():
    print("hello world ")

schedulers.start()
