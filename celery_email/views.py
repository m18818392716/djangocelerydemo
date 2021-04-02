from django.shortcuts import render
from .tasks import send_mail_task,plan_task_3
from django.http import HttpResponse

# Create your views here.
def sayhello(request):
    # 测试发送邮件
    title = '访问百度'
    msg = '<a href="http://www.baidu.com/" target="_blank">访问百度</a>'
    email = 'm18818392716@163.com'
    # send_mail_task.delay(title,email,msg) # 使用delay调用任务
    send_mail_task(title,email,msg) # 使用delay调用任务
    return HttpResponse("hello world")



# 首先说下异步任务执行delay()和apply_anysc()两者区别，
# 其实两者都是执行异步任务的方法，delay是apply_anysc的简写。
# 所以delay中传递的参数会比apply_anysc能传的参数少一些。那么延迟执行异步任务的关键点就在于传递的参数中。
from datetime import datetime,timedelta
def plant_task_3(request):
    eta = datetime.utcnow() + timedelta(seconds=10)
    # plan_task_3.apply_anysc(args=(),eta=eta, expires=60, retry=True)
    plan_task_3.apply_anysc(args=('test'))



#创建日志输出器
# logger = logging.getLogger('django')
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



