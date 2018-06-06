from django.db import models

# Create your models here.
class user (models.Model):
    name = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    token = models.TextField(null=True)
    status = models.CharField(max_length=32,null=True)


class host (models.Model):
    hostName = models.CharField(max_length=32)
    hostUrl = models.CharField(max_length=32)

class interfaceUrl(models.Model):
    nameUrl = models.CharField(max_length=32)
    addressUrl = models.CharField(max_length=32)

class commodity(models.Model):
    commoName = models.CharField(max_length=32)
    commoPrice = models.CharField(max_length=32)
    commoInfo = models.CharField(max_length=32)
    status = models.CharField(max_length=32)