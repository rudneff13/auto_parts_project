from django.contrib import admin

from .models import Truck, Product, ProductTruck


class ProductTruckInLine(admin.TabularInline):
    model = ProductTruck
    extra = 1


@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_products')
    inlines = (ProductTruckInLine,)
    list_filter = ('products',)
    search_fields = ('name', 'products__name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'get_trucks')
    inlines = (ProductTruckInLine,)
    list_filter = ('trucks',)
    search_fields = ('name', 'description', 'trucks__name',)
