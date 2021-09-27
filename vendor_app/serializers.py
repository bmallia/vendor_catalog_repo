from django.db.models import fields
from rest_framework import serializers
from .models import Product, Vendor

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class VendorSerializer(serializers.ModelSerializer):

     class Meta:
         model = Vendor
         fields = '__all__'