from django.contrib import admin

from .models import Vendor, Product

class VendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cnpj', 'city')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    fields = ["name", "cnpj", "city"]
    list_per_page = 20


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', "name", "code", "price", "vendor")
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Vendor, VendorAdmin)
admin.site.register(Product, ProductAdmin)