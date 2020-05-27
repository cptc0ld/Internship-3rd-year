from django.urls import path
from django.contrib import admin
from . import views

app_name = 'market'

urlpatterns = [
    path("market/", views.market, name='market'),
    path("sellitem/", views.sellitem, name='sellitem'),
]