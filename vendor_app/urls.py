from os import name
from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from rest_framework import routers
from django.urls import re_path

from .views import VendorViewSet, ProductViewSet, ListVendorViewSet, ListProductViewSet



router = routers.DefaultRouter()
router.register('product', ProductViewSet, basename='product')
router.register('vendor', VendorViewSet, basename='vendor')


urlpatterns = [
    path('', include(router.urls)),
    ##vendors patterns
    re_path("^vendorSearch/(?P<id>\d+)$", ListVendorViewSet.as_view(), {'cnpj': str(None), 'name': str(None), 'city':str(None)}, name="vendor-search"),    
    re_path("^vendorSearch/(?P<cnpj>\d{14})$", ListVendorViewSet.as_view(), { 'name': str(None), 'city':str(None), 'id': str(None)}),
    re_path("^vendorSearch/(?P<cnpj>\d{14})/(?P<name>[\w-]+)$", ListVendorViewSet.as_view(), {'city': str(None)}),
    re_path("^vendorSearch/(?P<cnpj>\d{14})/(?P<name>[\w-]+)/(?P<city>[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ'\s]+)$", ListVendorViewSet.as_view()),
    
    ##product patterns
    re_path("^productSearch/(?P<id>\d+)$", ListProductViewSet.as_view(), {'name': str(None), 'code': str(None), 'price': str(None)}),
    re_path("^productSearch/(?P<name>)[\w-]+$", ListVendorViewSet.as_view(), {'id': str(None), 'code': str(None), 'price': str(None)}),
    re_path("^productSearch/(?P<name>)[\w-]+/(?P<code>)[\d+]$", ListVendorViewSet.as_view(), {'id': str(None),'price': str(None)})
]
