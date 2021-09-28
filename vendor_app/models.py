from django.db import models
from django.db.models.fields import CharField


class Product(models.Model):

    class Meta:
        db_table = 'product'
    
    
    name = models.CharField(max_length=255)
    code = models.IntegerField(null=False)
    price = models.DecimalField(decimal_places=2, max_digits=10, blank=True)

    def __str__(self):
        return self.name

class Vendor(models.Model):

    class Meta:
        db_table = 'vendor'

    name= CharField(max_length=255)
    cnpj = CharField(max_length=14, unique=True)
    city = CharField(max_length=255,blank=True)
    
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name
