from django.views import generic

from .models import Truck, Product, ProductTruck
from .forms import ProductForm, TruckForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from .forms import FilterTruckForm

from .serializers import TruckSerializer, ProductSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters


class IndexView(generic.ListView):
    template_name = 'truck_parts_app/index.html'
    context_object_name = 'list_of_trucks'
    model = Truck

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = Truck.objects.filter(name__icontains=query)
        else:
            object_list = Truck.objects.all()
        return object_list


class TruckCreateView(generic.CreateView):
    model = Truck
    form_class = TruckForm
    template_name = 'truck_parts_app/truck-create-form.html'
    success_url = '/'


class TruckDetailView(generic.DetailView):
    model = Truck
    template_name = 'truck_parts_app/truck-detail.html'


class TruckUpdateView(generic.UpdateView):
    model = Truck
    form_class = TruckForm
    template_name = 'truck_parts_app/truck-update-form.html'

    def get_success_url(self):
        return reverse('truck_parts_app:truck-detail-form', args=(self.object.id,))


class TruckDeleteView(generic.DeleteView):
    model = Truck
    template_name = 'truck_parts_app/truck-confirm-delete.html'
    form_class = ProductForm
    success_url = '/'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'truck_parts_app/detail.html'


class ProductUpdateView(generic.UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'truck_parts_app/product-update-form.html'

    def get_success_url(self):
        return reverse('truck_parts_app:product-detail-form', args=(self.object.id,))


class ProductDeleteView(generic.DeleteView):
    model = Product
    template_name = 'truck_parts_app/product-confirm-delete.html'
    form_class = ProductForm
    success_url = '/products-list'


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
        return HttpResponseRedirect(reverse('truck_parts_app:product-detail-form', args=(prod.pk,)))
    else:
        form = ProductForm()
    return render(request, 'truck_parts_app/product-create-form.html', {'form': form})


class APITruckViewSet(ModelViewSet):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer
    search_fields = ['name', 'products__name']
    filter_backends = (filters.SearchFilter,)


class APIProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ['name', 'description', 'trucks__name']
    filter_backends = (filters.SearchFilter,)
