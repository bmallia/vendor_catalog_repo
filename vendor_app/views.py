from rest_framework import viewsets
from vendor_app.models import Product, Vendor
from vendor_app.serializers import ProductSerializer, VendorSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    Show the product's information

    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class VendorViewSet(viewsets.ModelViewSet):
    """
        Show the Vendor'S information
    Args:
        viewsets ([type]): [description]
    """
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer