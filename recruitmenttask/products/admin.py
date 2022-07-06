from django.contrib import admin
from .models import Product, Warehouse


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created']

#admin.site.register(Product)


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'created']
    list_filter = ['name']

#admin.site.register(Warehouse)
