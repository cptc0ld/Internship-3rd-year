from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from .models import CatItems, Item, Category, ItemCategory
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
    