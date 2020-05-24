from django.urls import path
from django.contrib import admin
from . import views

app_name = 'invo'

urlpatterns = [
    path("inventory/<steamid>/", views.invo, name='invo'),
    path("inventory/", views.invo, name='invo'),
]