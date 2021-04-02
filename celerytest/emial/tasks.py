# from django.core.mail import send_mail
# from django.conf import settings
# from djangocelerydemo.celeryconfig import app
#
# @app.task(name='send_verify_email', base= Mytask) #name 起别名  #base的值为监听的那个类
# def send_verify_email(to_email,verify_url):
#     """定义发送邮件的任务"""
#     # send_mail('标题','普通邮件的正文','发件人','收件人列表','富文本邮件正文')
#     subject = '填主题'
#     #message = '普通文本'
#     #html_message是发送带html样式信息
#     html_message = '<p>尊敬的用户您好！</p>' \
#                    '<p>感谢您使用xxxx。</p>' \
#                    '<p>您的邮箱为：%s 。请点击此链接激活您的邮箱：</p>' \
#                    '<p><a href="%s">%s<a></p>' % (to_email, verify_url, verify_url)
#     send_mail(subject,'',settings.EMAIL_FROM,[to_email],html_message=html_message)
#
#
#
# from celery.task import Task
# # 监听整个任务的钩子
# class Mytask(Task):
#     def on_success(self, retval, task_id, args, kwargs):
#         print('task success 11111')
#         return super(Mytask, self).on_success(retval, task_id, args, kwargs)
#
#     def on_failure(self, exc, task_id, args, kwargs, einfo):
#         print('task failed')
#         # 可以记录到程序中或者任务队列中,让celery尝试重新执行
#         return super(Mytask, self).on_failure(exc, task_id, args, kwargs, einfo)
#
#     def after_return(self, status, retval, task_id, args, kwargs, einfo):
#         print('this is after return')
#         return super(Mytask, self).after_return(status, retval, task_id, args, kwargs, einfo)
#
#     def on_retry(self, exc, task_id, args, kwargs, einfo):
#         print('this is retry')
#         return super(Mytask,self).on_retry(exc, task_id, args, kwargs, einfo)
