from django.db import models
import time

#用户基础表
class user(models.Model):
    userName = models.CharField(max_length=32,null=True)
    userPhone = models.CharField(max_length=32,null=True)
    status = models.IntegerField(max_length=32, default=1)
    create_time = models.DateTimeField(default=time.time())
    update_time = models.DateTimeField(default=time.time())

#用户信息表
class userInfo(models.Model):
    userId = models.IntegerField(max_length=32,null=True)
    token = models.TextField(null=True)
    openid = models.TextField(null=True)
    create_time = models.DateTimeField(default=time.time())
    update_time = models.DateTimeField(default=time.time())

#用户formID表
class userFromId(models.Model):
    userId = models.IntegerField(null=True)
    userFromId = models.CharField(max_length=32,null=True)
    status = models.IntegerField(max_length=32, default=1)
    create_time = models.DateTimeField(default=time.time())
    update_time = models.DateTimeField(default=time.time())

#accessToken表
class accessToken(models.Model):
    access_token = models.TextField(null=True)
    status = models.IntegerField(max_length=32, default=1)
    create_time = models.DateTimeField(default=time.time())
    update_time = models.DateTimeField(default=time.time())

#服务器地址表
class hostInfo(models.Model):
    hostName = models.CharField(max_length=32,null=True)
    hostUrl = models.CharField(max_length=32,null=True)
    status = models.IntegerField(max_length=32, default=1)
    create_time = models.DateTimeField(default=time.time())
    update_time = models.DateTimeField(default=time.time())

#接口地址表
class interfaceInfo(models.Model):
    interfaceName = models.CharField(max_length=32,null=True)
    interfaceUrl = models.CharField(max_length=32,null=True)
    status = models.IntegerField(max_length=32, default=1)
    create_time = models.DateTimeField(default=time.time())
    update_time = models.DateTimeField(default=time.time())