from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from .models import CatItems, Item, Category, ItemCategory
from authentication.models import SteamUser
import json
from inventory import urls
# Create your views here.

def market(request):
    items = Item.objects.all()
    cat = Category.objects.all()
    cartitems = CatItems.objects.all()
    return render(request, 'market.html', {'items': items, 'cat' : cat, 'cartitems': cartitems})
    

def sellitem(request):
    data = request.POST.get("data")
    data2 = request.POST.get("data2")
    price = request.POST.get("price")
    if(data):
        data = eval(data)
        assetid = data["items"][0]["assetid"]
        no_of_item = Item.objects.filter(assetid = assetid).count()
        if(no_of_item):
            return HttpResponse("already exist")
        else:
            item = Item.objects.createitem(data,price, 0)
            item.save()
            return redirect('/')
    else:
        index = (int(data2[-1]) -1)
        data2 = eval(data2[:-1])
        no_of_item = Item.objects.filter(assetid = data2["items"][index]["assetid"]).count()
        if(no_of_item):
            return HttpResponse("already exist")
        else:
            item = Item.objects.createitem(data2,price, index)
            item.save()
            return redirect('/')
        return HttpResponse("more than 1 items")

def sortByWeapons(request):
    weaponname = request.GET.get('weaponname', None)
    filteredItem = ItemCategory.objects.filter(weapon_name = weaponname).values()
    return JsonResponse(list(filteredItem), safe=False)

def getPrice(request):
    assetid = request.GET.get('assetid', None)
    contextid = request.GET.get('contextid', None)
    appid = request.GET.get('appid', None)

    filteredItem = Item.objects.filter(assetid = assetid).values()
    # print(filteredItem) 
    return JsonResponse(list(filteredItem), safe=False)

def purchseitem(request):
    assetid = request.GET.get('assetid', None)
    contextid = request.GET.get('contextid', None)
    appid = request.GET.get('appid', None)
    filteredItem = Item.objects.filter(assetid = assetid).values()
    if(len(filteredItem)):
        message = ""
        code = 0
        print("avalaible")
        steamid = request.GET.get('steamid', None)
        try:
            user = SteamUser.objects.get(steamid = steamid)
        except:
            message += "| There is some error."
            code = 0

        try:
            if(user.current_balance > filteredItem[0]['price']):
                message = "Balance is deducted, User will send you the Trade"
                code = 1
                user.withdraw(filteredItem[0]['price'])
            else:
                message += "| Insufficiant balance"
        except:
            message += "| There is some error. Balance is not deducted"
            code = 0
    else:
        print("not availables")
    resonsejson = '''{
        "status" : '''+ str(code) + ''',
        "message": '''+ str(message) + '''
    }'''
    return JsonResponse(resonsejson, safe=False)
