from django.db import models

# Create your models here.

class UserInfo(models.Model):
    #id列，自增
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
