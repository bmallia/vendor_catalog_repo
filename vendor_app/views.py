from rest_framework import viewsets, generics
from rest_framework.response import Response
from vendor_app.models import Product, Vendor
from vendor_app.serializers import ProductSerializer, VendorSerializer, ListProductVendorSerializer
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

    def create(self, request, *args, **kwargs):
        data = request.data
        new_vendor = Vendor.objects.create(name=data['name'], cnpj=data['cnpj'], city=data['city'])
        new_vendor.save()

        for product in data['products']:
            product_obj = Product.objects.get(code=product['code'])
            new_vendor.products.add(product_obj)
        
        serializer = VendorSerializer(new_vendor)
        return Response(serializer.data)

class ListVendorProductViewSet(generics.ListAPIView):
    """ Listing vendors and related products """
    
    def get_queryset(self):
        
        queryset = Vendor.objects.filter(id=self.kwargs['pk'])
        return queryset

    serializer_class = ListProductVendorSerializer
    