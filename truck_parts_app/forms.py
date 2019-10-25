from django import forms
from .models import Truck, Product
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm


class TruckForm(ModelForm):
    class Meta:
        model = Truck
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        super(TruckForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save truck'))


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
