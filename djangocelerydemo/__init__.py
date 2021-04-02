# 引入celery实例对象
from __future__ import absolute_import, unicode_literals # 是为了确保绝对路径导入的.
from djangocelerydemo.celeryconfig import app as celery_app

__all__ = ('celery_app',)

import pymysql
pymysql.version_info = (1, 4, 0, "final", 0)   # 指定版本
pymysql.install_as_MySQLdb()