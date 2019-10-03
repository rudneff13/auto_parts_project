from django.forms import ModelForm

from .models import Product, Truck


class TruckForm(ModelForm):
    class Meta:
        model = Truck
        fields = ('name', 'products')


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'trucks')
