from django.contrib import admin

from market.models import Category, Market, Item, CatItems


@admin.register(Category, Market, Item, CatItems)
class MarketAdmin(admin.ModelAdmin):
    pass
