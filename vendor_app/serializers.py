from django.db.models import fields
from rest_framework import serializers
from .models import Product, Vendor

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class VendorSerializer(serializers.ModelSerializer):
    """serializing vendors"""
    products = ProductSerializer(read_only=False, many=True)
    
    class Meta:
        model = Vendor
        fields = '__all__'
        depth = 1


    def validate(self, attrs):

        if (not Product.objects.filter(cpnj=attrs['cnpj']).exists()):
            raise serializers.ValidationError('Já existe este CNPJ cadastrado')
        
        return attrs

class ListProductVendorSerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=False, required=False, many=True)
    class Meta:
        model = Vendor
        ordering = ['name']
        exclude = ['id']
    
    