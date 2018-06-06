"""Tester URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from app import views,index,Tester
from app.controller import wecatController

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userCreat/', views.UserCreat),
    path(r'', index.index),
    path(r'test',Tester.Tester),
    path(r'getOpenId',wecatController.getOpenId),
    path(r'addHost',wecatController.addHost),
    path(r'secHost',wecatController.secHost),
    path(r'secUser',wecatController.secUser),
    path(r'addUser',wecatController.addUser)
    # path(r'postTest',wecatController.postTest)
]
