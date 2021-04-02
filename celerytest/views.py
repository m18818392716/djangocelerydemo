from django.shortcuts import render
from django.http import JsonResponse
from celerytest import tasks
# Create your views here.

from django.utils.safestring import mark_safe

pageHtml = mark_safe("你的html代码")
# 前端页面直接使用
# {{pageHtml}}
# 即可。
# mark_safe这个函数就是确认这段函数是安全的，不是恶意攻击的。

def demo_crsf(request):
    return render(request,'demo_crsf.html')

def index(request,*args,**kwargs):
    res=tasks.add.delay(1,3)
    #任务逻辑
    return JsonResponse({'status':'successful','task_id':res.task_id})


# from celery.utils.log import get_task_logger
# #创建日志输出器
# logger = logging.getLogger('django')
#
# class EmailView(LoginRequiredJSONMixin,View):
#     """添加邮箱"""
#     def put(self,request):
#         #接收参数
#         json_str = request.body.decode()
#         json_dict = json.loads(json_str)
#         email = json_dict.get('email')
#         #校验参数
#         if not email:
#             return HttpResponseForbidden('缺少email参数')
#         if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
#             return HttpResponseForbidden('参数email有误')
#         # 将用户传入的邮箱保存到用户数据库的email字段中
#         try:
#             request.user.email = email
#             request.user.save()
#         except Exception as e:
#             logger.error(e)
#             return JsonResponse({'code':RETCODE.DBERR,'errmsg':'添加邮箱失败'})
#
#         #发送邮箱验证邮件   这里是调用邮件的
#         verify_url = 'www.baidu.com'
#         send_verify_email.delay(email,verify_url) #一定要加delay!!!!
#
#         return JsonResponse({'code':RETCODE.OK,'errmsg':'OK'})


from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse

def send(request):
    email = "m18818392716@163.com"
    # 发邮件
    subject = '天天生鲜欢迎信息'
    message = '邮箱正文'
    sender = settings.EMAIL_FROM
    receiver = [email]
    send_mail(subject, message, sender, receiver)
    return HttpResponse('ok')