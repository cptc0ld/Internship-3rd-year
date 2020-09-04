from django.urls import path
from market.api import views

app_name = 'marketapi'

urlpatterns = [
    path('trade/', views.Trade.as_view()),
]
