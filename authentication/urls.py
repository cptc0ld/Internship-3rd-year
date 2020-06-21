from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path
from authentication.views import IndexView, LogoutView
from . import views
app_name = 'auth'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^logout', login_required(LogoutView.as_view(), login_url='/'), name='logout'),
    path("tradelink/<steamid>/", views.tradelink, name='tl'),
    path("tradelink/", views.tradelink, name='tl'),
    path("savetl/<steamid>/", views.savetl, name='savetl'),
    path("notification/", views.getNotification, name='notification'),
]
