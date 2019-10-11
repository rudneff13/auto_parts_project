from django import forms
from django.forms import ModelForm
from .models import Truck


# from django.forms import ModelForm
#
# from .models import Product, Truck
#

# class TruckForm(ModelForm):
#     class Meta:
#         model = Truck
#         fields = ('name', 'products')
#
#
# class ProductForm(ModelForm):
#     class Meta:
#         model = Product
#         fields = ('name', 'description', 'trucks')


class NameForm(forms.Form):
    hard_truck = forms.BooleanField(label='Hurd_truck_100', required=False)
    zil = forms.BooleanField(label='Zil_3000', required=False)


class TruckForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(TruckForm, self).__init__(*args, **kwargs)
        for truck in Truck.objects.all():
            self.fields[truck.name] = forms.BooleanField(required=False)

