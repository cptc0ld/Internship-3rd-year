from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator

import requests 
import json 
from authentication.models import SteamUser
# Create your views here.

def invo(request, steamid = None):
    if(steamid):
        URL = "https://steamcommunity.com/inventory/" + steamid + "/730/2"
        user = SteamUser.objects.get(steamid = steamid)
        # return HttpResponse(str(user.steamid))
        response = requests.get(URL)
        j = response.json()
        context1 = list()
        context2 = list()
    # try:
        for x in j['assets']:
            assets = dict()
            assets['steamid'] = steamid
            assets['personaname'] = user.personaname
            assets['profileurl'] = user.profileurl
            assets['avatar'] = user.avatar
            assets['avatarmedium'] = user.avatarmedium
            assets['avatarfull'] = user.avatarfull
            assets["appid"] = x["appid"]
            assets["contextid"] = x["contextid"]
            assets["assetid"] = x["assetid"]
            assets["classid"] = x["classid"]
            assets["instanceid"] = x["instanceid"]
            assets["amount"] = x["amount"]
            context2.append(assets)
        for x in j['descriptions']:
            description = dict()
            description['appid'] = x['appid']
            description['classid'] = x['classid']
            description['instanceid'] = x['instanceid']
            description['icon_url'] = x['icon_url']
            description['name'] = x['name']
            description['market_name'] = x['market_name']
            description['tradable'] = x['tradable']
            description['items'] = list()
            context1.append(description)

        for x in context1:
            items = list()
            for y in context2:
                if(x["classid"] == y["classid"]):

                    x['steamid'] = y['steamid']
                    x['personaname'] = y['personaname']
                    x['profileurl'] = y['profileurl']
                    x['avatar'] = y['avatar']
                    x['avatarmedium'] = y['avatarmedium']
                    x['avatarfull'] = y['avatarfull']
                    x["contextid"] = y["contextid"]

                    
                    details = {'assetid' : y["assetid"], 'amount' : y["amount"]}
                    items.append(details)
                    x['items'] = items
                    # x["assetid"] = y["assetid"]
                    # x["amount"] = y["amount"]

        context2.sort(key = lambda i: i['classid'])


        paginator = Paginator(context1, 20) # Show 25 contacts per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
            
        content = {
            'data' : page_obj
        }
        print(page_obj)
        return render(request, 'inventory.html', content)
    # except:
            # return HttpResponse(str(response) + URL)
    else:
        return redirect('auth:index')