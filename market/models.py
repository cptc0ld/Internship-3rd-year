from django.db import models

# Create your models here.
def getWeaponName(x):
    return x.split(' |')[0]
def getWear(x):
    return x.split('(')[1][:-1]
    
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

class ItemCategoryManager(models.Manager):
    def createitemcategory(self, data):
        itemcategory = self.model(name = data['name'])
        itemcategory.weapon_name = getWeaponName(data['market_name'])
        itemcategory.wear = getWear(data['market_name'])
        itemcategory.icon_url = data['icon_url']
        itemcategory.save()
        return itemcategory
class ItemCategory(models.Model):
    name = models.CharField(max_length=255)
    wear = models.CharField(max_length=255)
    weapon_name = models.CharField(max_length=255)
    icon_url = models.SlugField(max_length=255)
    objects = ItemCategoryManager()
class ItemManager(models.Manager):
    def createitem(self, data,price, i):
        itemcategory = ItemCategory.objects.createitemcategory(data)
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
        item.price = price
        item.icon_url = data['icon_url']
        item.category = itemcategory
        item.market_name = data['market_name']
        return item
class Item(models.Model):
    category = ItemCategory()
    steamid = models.CharField(max_length=17)
    market_name = models.CharField(max_length=255)
    icon_url = models.SlugField(max_length=255)
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
    price = models.IntegerField() 
    objects = ItemManager()

