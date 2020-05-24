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
        context = list()
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
            context.append(description)
        content = {
            'data' : context
        }
        # print(len(context))
        return render(request, 'inventory.html', content)
    else:
        return redirect('auth:index')