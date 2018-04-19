from django.db import models

# Create your models here.
class user (models.Model):
    name = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)


class host (models.Model):
    hostName = models.CharField(max_length=32)
    hostUrl = models.CharField(max_length=32)

class interfaceUrl(models.Model):
    nameUrl = models.CharField(max_length=32)
    addressUrl = models.CharField(max_length=32)