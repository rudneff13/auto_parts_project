from django.urls import path

# from .views import IndexView, ProductsListView, ProductDetailView
from .views import IndexView, ProductDetailView, ProductUpdateView, get_products, create_product

app_name = 'truck_parts_app'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products-list/', get_products, name='products-list'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    path('product-create-form', create_product, name='product-create-form'),
    path('product/<int:pk>-update-form', ProductUpdateView.as_view(), name='product-update-form'),
    # path('truck-create-form', TruckCreateView.as_view(), name='truck-create-form'),

]
