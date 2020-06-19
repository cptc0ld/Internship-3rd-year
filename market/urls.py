from django.urls import path
from django.contrib import admin
from . import views

app_name = 'market'

urlpatterns = [
    path("market/", views.market, name='market'),
    path("sellitem/", views.sellitem, name='sellitem'),
    path("sortByWeapons/", views.sortByWeapons, name='sortByWeapons'),
    path("getPrice/", views.getPrice, name='getPrice'),
    path("purchseitem/", views.purchseitem, name='purchseitem'),
]