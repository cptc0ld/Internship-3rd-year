from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
import json
from authentication.models import SteamUser
# Create your views here.


def balance(request):
    return render(request, 'wallet.html')


def getbalance(request):
    steamid = request.GET.get('steamid', None)
    try:
        filteredItem = SteamUser.objects.get(steamid=steamid)
    except SteamUser.DoesNotExist:
        return JsonResponse('{"Message" : "Login Required" }', safe=False)
    return JsonResponse('{"steamid" : ' + steamid + ', "balance": ' + str(filteredItem.current_balance) + '}', safe=False)
