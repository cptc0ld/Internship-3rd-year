from django.contrib import admin

from market.models import Category, Market


@admin.register(Category, Market)
class MarketAdmin(admin.ModelAdmin):
    pass
