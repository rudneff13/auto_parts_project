from django.urls import path

# from .views import IndexView, ProductsListView, ProductDetailView
from .views import IndexView, ProductDetailView, get_name

app_name = 'truck_parts_app'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products-list/', get_name, name='products-list'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='detail'),
]
