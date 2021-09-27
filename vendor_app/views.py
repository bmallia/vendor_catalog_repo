from rest_framework import viewsets
from vendor_app.models import Product, Vendor
from vendor_app.serializers import ProductSerializer, VendorSerializer
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    """
        Define the pagination config for REST services

    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ProductViewSet(viewsets.ModelViewSet):
    """
    Show the product's information

    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination


class VendorViewSet(viewsets.ModelViewSet):
    """
        Show the Vendor'S information
    """
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    pagination_class = StandardResultsSetPagination