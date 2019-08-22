#start file
from celery import Celery

#tell celery use django's settings file
import os
if not os.getenv("DJANGO_SETTINGS_MODULE"):
    os.environ["DJANGO_SETTINGS_MODULE"]="webbacksoftware.settings.settings"

#create app

app=Celery('hermit')

#import celery seeting file

app.config_from_object('celery_tasks.config')

#where to find task

app.autodiscover_tasks(['celery_tasks.msg_code','celery_tasks.email'])