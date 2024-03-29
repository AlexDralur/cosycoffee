from django.db import models

# Create your models here.


class Recipe(models.Model):
    """Recipe Model"""
    brewing_type = models.CharField(max_length=254, null=True, blank=True)
    coffee_quantity = models.DecimalField(max_digits=6, decimal_places=2)
    cups = models.IntegerField(default=0)
    grinding_size = models.CharField(max_length=254, null=True, blank=True)
    water_quantity = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(default='')

    def __str__(self):
        return self.name