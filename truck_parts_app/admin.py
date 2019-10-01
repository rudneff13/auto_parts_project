from django.contrib import admin

from .models import Truck, Product, ProductTruck


class ProductTruckInLine(admin.TabularInline):
    model = ProductTruck
    extra = 1


class TruckAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_products')
    inlines = (ProductTruckInLine,)
    list_filter = ('products',)
    search_fields = ('name', 'products__name')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'get_trucks')
    inlines = (ProductTruckInLine,)
    list_filter = ('trucks',)
    search_fields = ('name', 'description', 'trucks__name',)


admin.site.register(Truck, TruckAdmin)
admin.site.register(Product, ProductAdmin)

