from django.contrib import admin
from products.models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'precio']
    search_fields = ['name']

admin.site.register(Product, ProductAdmin)