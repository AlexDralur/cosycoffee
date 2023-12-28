from django.db import models

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    producers_name = models.TextField()
    region = models.CharField(max_length=254, null=True, blank=True)
    notes = models.CharField(max_length=254, null=True, blank=True)
    brand = models.CharField(max_length=254, null=True, blank=True)
    variety = models.CharField(max_length=254, null=True, blank=True)
    processing_method = models.CharField(max_length=254, null=True, blank=True)
    image_url = models.URLField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    rates = models.DecimalField(max_digits=6, decimal_places=2)
    price_ac = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    price_250g = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    price_1kg = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name
