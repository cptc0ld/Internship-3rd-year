from django.db import models

# Create your models here.

class Category(models.Model):
    appid = models.CharField(max_length=3)
    contextid = models.CharField(max_length=30)
    classid = models.CharField(max_length=30)
    icon_url = models.SlugField(max_length=255)
    market_name = models.CharField(max_length=255)

class Market(models.Model):
    USERNAME_FIELD = 'steamid'

    steamid = models.CharField(max_length=17, unique=True)
    personaname = models.CharField(max_length=255)
    profileurl = models.CharField(max_length=300)
    avatar = models.CharField(max_length=255)
    avatarmedium = models.CharField(max_length=255)
    avatarfull = models.CharField(max_length=255)
    appid = models.CharField(max_length=3)
    contextid = models.CharField(max_length=30)
    assetid = models.CharField(max_length=30)
    classid = models.CharField(max_length=30)
    instanceid = models.CharField(max_length=30)
    icon_url = models.SlugField()
    market_name = models.CharField(max_length=255)
    tradable = models.BooleanField()
