from django.contrib import admin

from .models import Vendor, Product

class VendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cnpj', 'city')
    list_display_links = ('id', 'name')
    search_fields = ('id','name',)
    fields = ["id","name", "cnpj", "city", "products"]
    list_per_page = 20


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', "name", "code", "price")
    list_display_links = ('id', 'name')
    search_fields = ('id','name',)
    list_per_page = 20

admin.site.register(Vendor, VendorAdmin)
admin.site.register(Product, ProductAdmin)