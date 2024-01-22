from django.db import models


class Producer(models.Model):
    """Class to add producers"""

    name = models.CharField(max_length=254)
    location = models.CharField(max_length=254)
    farm_name = models.CharField(max_length=254, null=True, blank=True)
    altitude = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
