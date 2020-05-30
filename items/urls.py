from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path
from authentication.views import IndexView, LogoutView
from . import views
app_name = 'item'

urlpatterns = [
    path("category/", views.cat, name='cat'),
]
