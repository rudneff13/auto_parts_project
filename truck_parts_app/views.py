from django.views import generic
from django.shortcuts import get_object_or_404

from .models import Truck, Product, ProductTruck
from .forms import ProductForm


class IndexView(generic.ListView):
    template_name = 'truck_parts_app/index.html'
    context_object_name = 'list_of_trucks'

    # search_fields = ('name', 'products__name')

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
from .forms import FilterTruckForm


def get_products(request):
    if request.method == 'POST':
        form = FilterTruckForm(request.POST)
        if form.is_valid():
            data = [k for k, v in form.cleaned_data.items() if v is True]
            new_data = '?filter=' + ','.join(data)
            return HttpResponseRedirect('' + new_data)

    else:
        getting_filtered = request.GET.get('filter', '').split(',')
        start_dict = {}
        for truck in Truck.objects.all():
            if truck.name in getting_filtered:
                start_dict[truck.name] = True
        form = FilterTruckForm(initial=start_dict)

        # new_filter = Product.objects.all()
        # new_filter.filter(trucks__name__in=start_dict)

        new_filter = set(Product.objects.all().filter(trucks__name__in=start_dict))

    return render(request, 'truck_parts_app/products_list.html',
                  {'form': form, 'products': new_filter})


# class ProductCreateView(generic.CreateView):
#     form_class = ProductForm
#     model = Product
#     # fields = ('name', 'description', 'trucks')
#     template_name = 'truck_parts_app/product-create-form.html'
#     success_url = 'products-list'
#
#
class ProductUpdateView(generic.UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'truck_parts_app/product-update-form.html'
    # success_url = 'products-list'
    # pk_url_kwarg = 'pk'

    # def get_object(self):
    #     return Product.objects.get(pk='pk_url_kwarg')

    def get_success_url(self):
        return reverse('truck_parts_app:product-detail', args=(self.object.id,))
#
# class TruckCreateView(generic.CreateView):
#     model = Truck
#     # fields = ['name']
#     form_class = TruckForm
#     template_name = 'truck_parts_app/truck-create-form.html'
#     success_url = 'products-list'

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.save()
            for truck in Truck.objects.all():
                if truck in form.cleaned_data['trucks']:
                    new_obj = ProductTruck(product=prod, truck=truck)
                    new_obj.save()
        return HttpResponseRedirect(reverse('truck_parts_app:product-detail', args=(prod.pk,)))
    else:
        form = ProductForm()
    return render(request, 'truck_parts_app/product-create-form.html', {'form': form})
