from __future__ import absolute_import, unicode_literals #是为了确保绝对路径导入的.
import os

from celery import Celery, platforms
from django.utils.datetime_safe import datetime
from django.conf import settings

# 获取当前文件夹名，即为该 Django 的项目名
project_name = os.path.split(os.path.abspath('.'))[-1]
project_settings = '%s.settings' % project_name
print(project_settings)

# 设置默认celery命令行的环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangocelerydemo.settings')# 修改这一行将mypro换成你的项目名称

# 实例化 Celery,项目名称
app = Celery('djangocelerydemo')# 修改这一行将mypro换成你的项目名称

# 解决时区问题
app.now = datetime.now

# 使用 django 的 settings 文件配置 celery
app.config_from_object('django.conf:settings', namespace='CELERY')#  使用CELERY_ 作为前缀，在settings中写配置

# 从所有应用中加载任务模块tasks.py
app.autodiscover_tasks()# 自动识别每个app中的celery
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.autodiscover_tasks(['celerytest'], force=True)
app.autodiscover_tasks(['celery_email'], force=True)
app.autodiscover_tasks(['celerytest.periodic4'], force=True)

# 解决celery不能root用户启动的问题
platforms.C_FORCE_ROOT = True

# app.conf.update(
#     result_expires=3600,# 默认是一天
# )

@app.task(bind=True)
def debug_task(self):
    print('Request:{0!r}'.format(self.request))


# if __name__ == '__main__':
#     app.start()
