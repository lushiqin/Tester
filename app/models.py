from django.db import models
import time

#用户基础表
class user(models.Model):
    userName = models.CharField(max_length=32,null=True)
    userPhone = models.CharField(max_length=32,null=True)
    token = models.TextField(null=True)
    status = models.IntegerField(default=1)
    create_time = models.IntegerField(null=True)
    update_time = models.IntegerField(null=True)

#用户信息表
class userInfo(models.Model):
    userId = models.IntegerField(null=True)
    openid = models.TextField(null=True)
    create_time = models.IntegerField(null=True)
    update_time = models.IntegerField(null=True)

#用户formID表
class userFromId(models.Model):
    userId = models.IntegerField(null=True)
    userFromId = models.CharField(max_length=32,null=True)
    status = models.IntegerField(default=1)
    create_time = models.IntegerField(null=True)
    update_time = models.IntegerField(null=True)

#accessToken表
class accessToken(models.Model):
    access_token = models.TextField(null=True)
    status = models.IntegerField(default=1)
    create_time = models.IntegerField(null=True)
    update_time = models.IntegerField(null=True)

#服务器地址表
class hostInfo(models.Model):
    hostName = models.CharField(max_length=32,null=True)
    hostUrl = models.CharField(max_length=32,null=True)
    status = models.IntegerField(default=1)
    create_time = models.IntegerField(null=True)
    update_time = models.IntegerField(null=True)

#接口地址表
class interfaceInfo(models.Model):
    interfaceName = models.CharField(max_length=32,null=True)
    interfaceUrl = models.CharField(max_length=32,null=True)
    methodType = models.CharField(max_length=32,null=True)
    data = models.TextField(null=True)
    status = models.IntegerField(default=1)
    create_time = models.IntegerField(null=True)
    update_time = models.IntegerField(null=True)