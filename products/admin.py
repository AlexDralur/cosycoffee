from django.contrib import admin
from .models import Category, Product

# Register your models here.

admin.site.register(Category)


class ProductAdmin(admin.ModelAdmin):
    """Function to display the form in the order selected"""
    list_display = (
        'sku',
        'name',
        'processing_method',
        'rates',
        'price_250g',
        'price_1kg',
        'price_ac',
    )


admin.site.register(Product, ProductAdmin)