from django import forms
from .models import Truck, Product, ProductTruck
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, ButtonHolder, Layout, Fieldset, Button, Div, HTML, Field
from crispy_forms.bootstrap import FormActions

from django.urls import reverse

from django.forms import ModelForm


#
# from .models import Product, Truck


# class TruckForm(ModelForm):
#     class Meta:
#         model = Truck
#         fields = ('name',)


class FilterTruckForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(FilterTruckForm, self).__init__(*args, **kwargs)
        for truck in Truck.objects.all():
            self.fields[truck.name] = forms.BooleanField(required=False)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Filter'))


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'description', 'trucks']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['trucks'].widget = forms.widgets.CheckboxSelectMultiple()
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save product'))


# class SearchForm(forms.Form):
#     keyword = forms.CharField(required=False, max_length=50)
