from django.db.models import fields
from rest_framework import serializers
from .models import Product, Vendor

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class VendorSerializer(serializers.ModelSerializer):
    """serializing vendors"""
   
    class Meta:
        model = Vendor
        fields = '__all__'
        depth = 1

    def validate(self, data):
        """
            Validate all necessary fields to validate vendor model

        Args:
            data ([vendor model]): [data vendor model]

        Raises:
            serializers.ValidationError: [raise a error for duplicate cnpj]

        Returns:
            [type]: [data vendor model]
        """
        cnpj_field = data.get('cnpj')

        if Vendor.objects.filter(cnpj=cnpj_field).exists():
            raise serializers.ValidationError({"error": True, 'detail': 'CNPJ já existente'})
        return data

class ListProductVendorSerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=False, required=False, many=True)
    class Meta:
        model = Vendor
        ordering = ['name']
        exclude = ['id']
    
    