from django.contrib import admin
from .models import Product, ShippingBox


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'length', 'width',
        'height', 'weight'
    )
    search_fields = ('name',)


@admin.register(ShippingBox)
class ShippingBoxAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'length', 'width',
        'height', 'max_weight', 'cost'
    )
    search_fields = ('name',)