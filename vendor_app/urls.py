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
    re_path("^vendorSearch/", ListVendorViewSet.as_view(), { 'cnpj': str(None), 'name': str(None), 'city':str(None)}),
    re_path("^vendorSearch/(?P<cnpj>\d{14})$", ListVendorViewSet.as_view(), { 'name': str(None), 'city':str(None)}),
    re_path("^vendorSearch/(?P<cnpj>\d{14})/(?P<name>[a-zA-Z0-9_ %]+)$", ListVendorViewSet.as_view(), {'city': str(None)}),
    re_path("^vendorSearch/(?P<name>[a-zA-Z0-9_ %]+)$", ListVendorViewSet.as_view(), {'cnpj': str(None),'city': str(None)}),
    re_path("^vendorSearch/(?P<cnpj>\d{14})/(?P<name>[\w-]+)/(?P<city>[a-zA-Z\u00C0-\u00FF]+)$", ListVendorViewSet.as_view())
    
    
    
]
