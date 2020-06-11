from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
import json
from authentication.models import SteamUser
# Create your views here.

def balance(request):
    return render(request, 'wallet.html')

def getbalance(request):
    steamid = request.GET.get('steamid', None)
    filteredItem = SteamUser.objects.get(steamid = steamid)
    return JsonResponse('{"steamid" : '+ steamid + ', "balance": ' + str(filteredItem.current_balance) + '}', safe=False)