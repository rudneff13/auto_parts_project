from django.views import generic

from .models import Truck, Product


class IndexView(generic.ListView):
    template_name = 'truck_parts_app/index.html'
    context_object_name = 'list_of_trucks'
    search_fields = ('name', 'products__name')

    def get_queryset(self):
        return Truck.objects.all()


# class ProductsListView(generic.ListView):
#     template_name = 'truck_parts_app/products_list.html'
#     search_fields = ('name', 'description', 'trucks__name',)
#     # context_object_name = 'list_of_products'
#
#     def get_queryset(self):
#         return {'product': Product.objects.all(),
#                 'truck': Truck.objects.all(),
#                 }
#
#     def get(self, request):
#         if request.method=='GET'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'truck_parts_app/detail.html'


from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, reverse, redirect
from .forms import TruckForm


def get_name(request):
    if request.method == 'POST':
        form = TruckForm(request.POST)
        if form.is_valid():
            data = [k for k, v in form.cleaned_data.items() if v is True]
            new_data = '?filter=' + ','.join(data)

            return HttpResponseRedirect('' + new_data)

    else:
        anything = request.GET.get('filter', '').split(',')

        start_dict = {}
        for truck in Truck.objects.all():
            if truck.name in anything:
                start_dict[truck.name] = True
        form = TruckForm(initial=start_dict)

        new_filter = Product.objects.filter(trucks__name__in=start_dict)

    return render(request, 'truck_parts_app/products_list.html',
                  {'form': form, 'products': new_filter})



# from django.http import HttpResponseRedirect, HttpResponse
# from django.shortcuts import render, reverse, redirect
# from .forms import NameForm
#
#
# def get_name(request):
#     if request.method == 'POST':
#         form = NameForm(request.POST)
#         if form.is_valid():
#             data = [k for k, v in form.cleaned_data.items() if v is True]
#             new_data = '?filter=' + ','.join(data)
#
#             return HttpResponseRedirect('' + new_data)
#
#     else:
#         anything = request.GET.get('filter', '').split(',')
#
#         start_dict = {}
#         for i in ['zil', 'hard_truck']:
#             if i in anything:
#                 start_dict[i] = True
#         form = NameForm(initial=start_dict)
#
#         new_filter = Product.objects.filter(trucks__name__in=start_dict)
#
#     return render(request, 'truck_parts_app/products_list.html',
#                   {'form': form, 'products': new_filter})
