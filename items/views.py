from django.contrib.auth import logout
from django.shortcuts import render, redirect
from . import models
from django.views import View
from django.http import HttpResponse


def cat(request):
    
    return render(request, 'category')