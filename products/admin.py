from django.contrib import admin
from .models import Category, Product

# Register your models here.

admin.site.register(Category)

class ProductAdmin(admin.ModelAdmin):
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