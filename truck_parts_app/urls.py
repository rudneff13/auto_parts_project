from django.urls import path

from .views import IndexView, ProductsListView, ProductDetailView

app_name = 'truck_parts_app'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products_list/', ProductsListView.as_view(), name='products_list'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='detail'),
]
