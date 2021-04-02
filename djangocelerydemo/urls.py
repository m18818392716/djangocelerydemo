"""djangocelerydemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from celerytest import views
from celery_email import views as emailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('send/', views.send),
    path('sayhello/', emailView.sayhello, name='sayhello'),
    path('task3/', emailView.plan_task_3, name='task3'),
    path('index2/',views.demo_crsf)
]
