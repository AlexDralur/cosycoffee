from django.db import models
from producers.models import Producer


class Category(models.Model):
    """Categories Model"""
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """Product Model"""
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField(default='')
    producers_name = models.ForeignKey(
        Producer, null=True, blank=True, on_delete=models.SET_NULL)
    notes = models.CharField(max_length=254, null=True, blank=True)
    brand = models.CharField(max_length=254, null=True, blank=True)
    variety = models.CharField(max_length=254, null=True, blank=True)
    processing_method = models.CharField(max_length=254, null=True, blank=True)
    image_url = models.URLField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    rates = models.DecimalField(max_digits=6, decimal_places=2)
    microlot = models.BooleanField(default=False)
    price_ac = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    price_250g = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    price_1kg = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name
