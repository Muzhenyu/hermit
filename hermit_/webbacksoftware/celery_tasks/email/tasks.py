from django.core.mail import send_mail
from django.conf import settings
from celery_tasks.main import app

@app.task()
def sendmail(email,url_str):
    send_mail(subject='shanghui email active', message=url_str, from_email=settings.EMAIL_FROM,
              recipient_list=[email], html_message=url_str)