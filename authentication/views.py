from django.contrib.auth import logout
from django.shortcuts import render, redirect
from . import models
from django.views import View
from django.http import HttpResponse
import notifications.models as noti
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('auth:index')

def tradelink(request, steamid = None):
    if(steamid):
        user = models.SteamUser.objects.get(steamid = steamid)
        return render(request, 'tradelink.html', {'url' : user.tradeurl})
    else:
        return redirect('auth:index')

def savetl(request, steamid):
    if(request.method == 'GET'):
            user = models.SteamUser.objects.get(steamid = steamid)
            user.tradeurl = request.GET.get("tradeurl")
            user.save()
            return redirect('auth:index')
            # user.set_url(tradelink)
            
    return HttpResponse("NOT saved")
