from django.views import generic

from .models import Truck, Product


class IndexView(generic.ListView):
    template_name = 'truck_parts_app/index.html'
    context_object_name = 'list_of_trucks'
    search_fields = ('name', 'products__name')

    def get_queryset(self):
        return Truck.objects.all()


class ProductsListView(generic.ListView):
    template_name = 'truck_parts_app/products_list.html'
    search_fields = ('name', 'description', 'trucks__name',)
    # context_object_name = 'list_of_products'

    def get_queryset(self):
        return {'product': Product.objects.all(),
                'truck': Truck.objects.all(),
                }

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(ProductsListView, self).get_context_data()
    #     context['products'] = Product.objects.all()


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'truck_parts_app/detail.html'
