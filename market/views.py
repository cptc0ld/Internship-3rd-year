from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from . import models
import json
from inventory import urls
# Create your views here.

def market(request):
    items = models.Item.objects.all()
    return render(request, 'market.html', {'items': items})


def sellitem(request):
    data=request.POST.get("data")
    data = eval(data)
    no_of_item = models.Item.objects.filter(assetid = data["assetid"]).count()
    print(no_of_item)
    if(no_of_item):
        return HttpResponse("already exist")
    else:
        item = models.Item.objects.createitem(data)
        item.save()
        return redirect('/')