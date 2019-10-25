from django.urls import path, include
from .views import IndexView, ProductDetailView, ProductUpdateView, ProductDeleteView, get_products, create_product, \
    TruckCreateView, TruckDeleteView, TruckDetailView, TruckUpdateView

from rest_framework.routers import DefaultRouter
from .views import APITruckViewSet, APIProductViewSet

router = DefaultRouter()
router.register('trucks', APITruckViewSet)
router.register('products', APIProductViewSet)


app_name = 'truck_parts_app'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products-list/', get_products, name='products-list'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product-detail-form'),
    path('product/<int:pk>-delete-form', ProductDeleteView.as_view(), name='product-delete-form'),
    path('product-create-form', create_product, name='product-create-form'),
    path('product/<int:pk>-update-form', ProductUpdateView.as_view(), name='product-update-form'),
    path('truck-create-form', TruckCreateView.as_view(), name='truck-create-form'),
    path('truck/<int:pk>', TruckDetailView.as_view(), name='truck-detail-form'),
    path('truck/<int:pk>-delete-form', TruckDeleteView.as_view(), name='truck-delete-form'),
    path('truck/<int:pk>-update-form', TruckUpdateView.as_view(), name='truck-update-form'),

    path('api/', include(router.urls))
]
