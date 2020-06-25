from django.urls import path
from . import views
app_name = 'tradehandler'

urlpatterns = [
    path("tradecheck/", views.tradecheck, name='tradecheck'),
]