from django.urls import path

from .views import IndexView, ProductsListView, ProductDetailView

app_name = 'truck_parts_app'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products-list/', ProductsListView.as_view(), name='products-list'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='detail'),
]
