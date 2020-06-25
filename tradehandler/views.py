from django.shortcuts import render, redirect
from django.http import HttpResponse
from authentication.models import SteamUser

# Create your views here.

def tradecheck(request):
    return HttpResponse("hello")