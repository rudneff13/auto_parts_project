from django.urls import path, include
from django.conf.urls import url
from .views import IndexView, ProductDetailView, ProductUpdateView, ProductDeleteView, get_products, create_product



# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework.renderers import CoreJSONRenderer
from .views import APITruckViewSet, APIProductViewSet

router = DefaultRouter()
router.register('trucks', APITruckViewSet)
router.register('products', APIProductViewSet)




# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
#
# schema_view = get_schema_view(
#    openapi.Info(
#       title="Snippets API",
#       default_version='v1',
#       description="Test description",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="contact@snippets.local"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )



# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!




app_name = 'truck_parts_app'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products-list/', get_products, name='products-list'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    path('product/<int:pk>-delete-form', ProductDeleteView.as_view(), name='product-delete-form'),
    path('product-create-form', create_product, name='product-create-form'),
    path('product/<int:pk>-update-form', ProductUpdateView.as_view(), name='product-update-form'),
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # path('truck-create-form', TruckCreateView.as_view(), name='truck-create-form'),
    # path('api/', include(router.urls)),
    # url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # url(r'^swagger/$', schema_view. with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # url(r'^', schema_view, name='docs'),
    # url(r'^api/', schema_view),
    # path('api/', APITrucks.as_view())
    path('api/', include(router.urls))
]
