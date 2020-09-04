"""steam_openid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import notifications.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('social_django.urls', namespace='social')),
    url(r'^', include('authentication.urls', namespace='auth')),
    url(r'^', include('inventory.urls', namespace='invo')),
    url(r'^', include('market.urls', namespace='market')),
    url(r'^', include('wallet.urls', namespace='wallet')),
    url(r'^', include('markettransactions.urls', namespace='markettransactions')),
    url(r'^', include('tradehandler.urls', namespace='tradehandler')),
    url(r'^api/', include('market.api.urls', namespace='marketapi')),
    url('^inbox/notifications/',
        include(notifications.urls, namespace='notifications')),
]


"""
URL pattern for notification
urlpatterns = [
    pattern(r'^$', views.AllNotificationsList.as_view(), name='all'),
    pattern(r'^unread/$', views.UnreadNotificationsList.as_view(), name='unread'),
    pattern(r'^mark-all-as-read/$', views.mark_all_as_read, name='mark_all_as_read'),
    pattern(r'^mark-as-read/(?P<slug>\d+)/$', views.mark_as_read, name='mark_as_read'),
    pattern(r'^mark-as-unread/(?P<slug>\d+)/$', views.mark_as_unread, name='mark_as_unread'),
    pattern(r'^delete/(?P<slug>\d+)/$', views.delete, name='delete'),
    pattern(r'^api/unread_count/$', views.live_unread_notification_count, name='live_unread_notification_count'),
    pattern(r'^api/all_count/$', views.live_all_notification_count, name='live_all_notification_count'),
    pattern(r'^api/unread_list/$', views.live_unread_notification_list, name='live_unread_notification_list'),
    pattern(r'^api/all_list/', views.live_all_notification_list, name='live_all_notification_list'),
]
"""
