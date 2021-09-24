from django.contrib import admin

from .models import Vendor, Product

class VendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cnpj', 'city')
    fields = ["name", "cnpj", "city"]

admin.site.register(Vendor, VendorAdmin)
