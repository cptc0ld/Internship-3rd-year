from django.contrib import admin

from market.models import Category, Market, Item, CatItems, ItemCategory


@admin.register(Category, Market, Item, CatItems, ItemCategory)
class MarketAdmin(admin.ModelAdmin):
    pass
