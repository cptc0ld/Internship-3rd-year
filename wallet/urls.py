from django.urls import path
from django.contrib import admin
from . import views

app_name = 'wallet'

urlpatterns = [
    path("balance/", views.balance, name='balance'),
    path("getbalance/", views.getbalance, name='getbalance'),
]