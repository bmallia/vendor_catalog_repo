from django.db.models.query import QuerySet
from django.db.models.sql import query
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

    def put(self, request, *args, **kwargs):
        pass

class VendorViewSet(viewsets.ModelViewSet):
    
    """
        Show the Vendor'S information
    """
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    pagination_class = StandardResultsSetPagination

    def create(self, request, *args, **kwargs):
        """
            Saving the vendor and the relalated product, the specification says doesn't pass
            id, so always will be a new product is this method
        """
        data = request.data
        new_vendor = {}
        serializer = VendorSerializer(Vendor, data=data)
        serializer.validate(data)
        if serializer.is_valid():
            new_vendor = Vendor.objects.create(name=data['name'], cnpj=data['cnpj'], city=data['city'])

            if data['products']:    
                for product in data['products']:
                    product_obj = Product.objects.create(code=product['code'], name=product['name'], price=product['price'])
                    product_obj.save()
                    new_vendor.products.add(product_obj)
            else:
                new_vendor.products.add([])

            new_vendor.save()   
        
        return Response({"error": False, "msg": "Vendor saved sucessfully"""})
        

class ListVendorViewSet(generics.ListAPIView):
    """ Listing vendors with many field: id, name, cnpj, city """
    serializer_class = ListProductVendorSerializer
    model = Vendor
    pagination_class = StandardResultsSetPagination
    
    
    def get_queryset(self):
        
           
        name_field = self.kwargs['name']
        cnpj_field = self.kwargs['cnpj']
        city_field = self.kwargs['city']

        args = {}

        if name_field != 'None':
            args['name'] = name_field

        if cnpj_field != 'None':
            args['cnpj'] = cnpj_field

        if city_field != 'None':
            args['city'] = city_field

        queryset = Vendor.objects.filter(**args)
        

        return queryset

class ListProductViewSet(generics.ListAPIView):
    """ List Product with mayfield (id, name, price, code) """
    serializer_class = ProductSerializer
    model = Product
    ##pagination_class = StandardResultsSetPagination

    def get_queryset(self):
       
        params = {}
        name_field = self.kwargs['name']
        price_field = self.kwargs['price']
        code_field = self.kwargs['code']

        if code_field:
            params['code'] = code_field
       
        if name_field:
           params['name'] = name_field
        
        if price_field:
            params['price'] = price_field

        queryset = Product.objects.filter(**params)
        return queryset