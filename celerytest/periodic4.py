# Celery4
# 新版的好处是，可以把定时任务和普通的任务一样单独定义了。多了 @app.on_after_configure.connect 这个装饰器，3版本是没有这个装饰器的。
# 写代码
# 单独再创建一个py文件，存放定时任务：

from __future__ import absolute_import, unicode_literals
from djangocelerydemo.celeryconfig import app
from celery.schedules import crontab


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # 每10秒执行一次
    sender.add_periodic_task(10.0, hello.s(), name='hello every 10')  # 给任务取个名字

    # 每30秒执行一次
    sender.add_periodic_task(30, upper.s('abcdefg'), expires=10)  # 设置任务超时时间10秒

    # 执行周期和Linux的计划任务crontab设置一样
    sender.add_periodic_task(
        crontab(hour='*', minute='*/2', day_of_week='*'),
        add.s(11, 22),
    )


@app.task
def hello():
    print('Hello World')


@app.task
def upper(arg):
    return arg.upper()


@app.task
def add(x, y):
    print("计算2个值的和: %s %s" % (x, y))
    return x + y


# 上面一共定了3个计划。
# name参数给计划取名，这样这个任务报告的时候就会使用name的值，像这样：hello every 10。否则默认显示的是调用函数的命令，像这样：CeleryPro.periodic4.upper('abcdefg') 。
# expires参数设置任务超时时间，超时未完成，可能就放弃了（没测试）。
# 修改一下之前的celery.py文件，把新写的任务文件添加到include的列表里。


# 这里Beat的-A参数用 CeleryPro 也能启动这里的定时任务。CeleryPro.tasks 效果也是一样的。另外如果把periodic4.py加到include列表里去，用 CeleryPro.periodic4 参数启动的话，这里的定时任务也会启动。
# 这里也是支持用crontab的，用法和之前的一样，把schedule参数的值换成调用crontab的函数。


# pip freeze > environment.txt
# python manage.py runserver
# celery -A djangocelerydemo flower   这是个监控定时任务的工具，用了方便一些，不用也无所谓
# celery -A djangocelerydemo worker --pool=solo -l info
# celery -A djangocelerydemo beat -l info    实现定时任务的动态操作（添加/删除）等，此插件本质是对数据库表变化做检查，一旦有数据库表改变，调度器重新读取任务进行调度
# 参考链接：https://blog.csdn.net/weixin_34414650/article/details/92112869

