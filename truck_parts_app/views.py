from django.views import generic

from .models import Truck, Product


class IndexView(generic.ListView):
    template_name = 'truck_parts_app/index.html'
    context_object_name = 'list_of_trucks'

    def get_queryset(self):
        return Truck.objects.all()


class ProductsListView(generic.ListView):
    template_name = 'truck_parts_app/products_list.html'
    context_object_name = 'list_of_products'

    def get_queryset(self):
        return Product.objects.all()


class ProductDetailView(generic.DetailView):
    template_name = 'truck_parts_app/detail.html'
    context_object_name = 'detail'

    def get_queryset(self):
        return Product.objects.all()
