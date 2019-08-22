from webbacksoftware.libs.yuntongxun.sms import CCP
from celery_tasks.main import app


@app.task()
def sendmsg(phone,msg):
    ccp = CCP()
    ret_data = ccp.send_template_sms(phone, [msg, '5'], 1)