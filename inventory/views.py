from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests 
import json 
# Create your views here.

def invo(request, steamid = None):
    if(steamid):
        URL = "https://steamcommunity.com/inventory/" + steamid + "/730/2"

        response = requests.get(URL)
        response = response.json()
        context1 = list()
        context2 = list()
        for x in response['assets']:
            assets = dict()
            assets["appid"] = x["appid"]
            assets["contextid"] = x["contextid"]
            assets["assetid"] = x["assetid"]
            assets["classid"] = x["classid"]
            assets["instanceid"] = x["instanceid"]
            assets["amount"] = x["amount"]
            context2.append(assets)
        for x in response['descriptions']:
            # print(x)
            description = dict()
            description['appid'] = x['appid']
            description['classid'] = x['classid']
            description['instanceid'] = x['instanceid']
            description['icon_url'] = x['icon_url']
            description['name'] = x['name']
            description['market_name'] = x['market_name']
            description['tradable'] = x['tradable']
            context1.append(description)

        for x in context2:
            for y in context1:
                if(x["classid"] == y["classid"]):
                    x["icon_url"] = y["icon_url"]
                    x["market_name"] = y["market_name"]
                    x["tradable"] = y["tradable"]

        content = {
            'data' : context2
        }
        # print(len(context))
        return render(request, 'inventory.html', content)
    else:
        return redirect('auth:index')