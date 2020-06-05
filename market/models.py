from django.db import models

# Create your models here.
def getWeaponName(x):
        return x.split(' |')[0]
    
class Category(models.Model):
    catname = models.CharField(max_length=255, unique = True)
    caticon = models.CharField(max_length=255)
    
class CatItems(models.Model):
    itemname = models.CharField(max_length=255)
    catname = models.CharField(max_length=255)
    
class Market(models.Model):
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


class ItemManager(models.Manager):
    

    def createitem(self, data, i):
        print(data)
        item = self.model(steamid = data['steamid'])
        item.personaname = data['personaname']
        item.profileurl = data['profileurl']
        item.avatar = data['avatar']
        item.avatarmedium = data['avatarmedium']
        item.appid = data['appid']
        item.contextid = data['contextid']
        item.assetid = data["items"][i]["assetid"]
        item.classid = data['classid']
        item.instanceid = data['instanceid']
        item.icon_url = data['icon_url']
        item.market_name = data['market_name']
        item.weapon_name = getWeaponName(data['market_name'])
        return item
class Item(models.Model):
    steamid = models.CharField(max_length=17)
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
    icon_url = models.SlugField(max_length=255)
    market_name = models.CharField(max_length=255)
    weapon_name = models.CharField(max_length=255)
    objects = ItemManager()
    
