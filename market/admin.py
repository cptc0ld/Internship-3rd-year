from django.contrib import admin

from market.models import Category, Market, Item


@admin.register(Category, Market, Item)
class MarketAdmin(admin.ModelAdmin):
    pass
