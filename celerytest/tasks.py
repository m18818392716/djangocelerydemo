# Create your tasks here
from __future__ import absolute_import, unicode_literals

from djangocelerydemo.celeryconfig import app


@app.task
def plan_task_1():
    print("任务_1已运行！")
    return {"任务_1:success"}


@app.task
def plan_task_2():
    print("任务_2已运行！")
    return {"任务_2:success"}

from celery import shared_task # 这个shared_task可以让你的任务在任何app中被调用.
from celery.schedules import crontab

@shared_task
def add(x,y):
    print("1+1")
    return x+y

@shared_task
def sub(x,y):
    print("1-1")
    return x-y

@shared_task
# 定义的定时任务函数
def auto_sc():
    print('sc test?')
    return 'halo'

# # name表示设置任务的名称，如果不填写，则默认使用函数名做为任务名
# 定义的两个异步函数
@shared_task(name="send_sms")
def send_sms():
    print("发送短信!!!")
    return "s"


@shared_task(name="send_sms2")
def send_sms2():
    print("发送短信任务2!!!")
    print("p")
    return "p"


from celery.utils.log import get_task_logger
from celery import task
@task
def test_celery(x, y):
    logger = get_task_logger(__name__)
    logger.info('func start  ----------------->')
    logger.info('application:%s', "TEST_APP")
    logger.info('func end -------------------->')
    print(x + y)
    return x + y


@task
def test_multiply(x, y):
    logger = get_task_logger(__name__)
    logger.info('func start  ----------------->')
    logger.info('application:%s', "TEST_APP")
    logger.info('func end -------------------->')
    print(x * y)
    return x * y


from django.core.mail import send_mail

@shared_task
def order_created():
    subject = '标题'
    message = '一句话'
    mail_sent = send_mail(subject, message,'发送邮箱号',['接收人邮箱号'])
    return mail_sent


