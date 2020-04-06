from django.db import models
from django.contrib.auth.models import User

class Manufacturer(models.Model):
    name = models.CharField(max_length=25)
    website = models.URLField(
        db_index=True, 
        unique=True, 
        blank=True
    )

class ShoeType(models.Model):
    style = models.CharField(max_length=25)

class ShoeColor(models.Model):
    CHOICES = [
    ('0', 'Red'),
    ('1', 'Orange'),
    ('2', 'Yellow'),
    ('3', 'Green'),
    ('4', 'Blue'),
    ('5', 'Indigo'),
    ('6', 'Violet'),
    ('7', 'Black'),
    ('8', 'White'),
    ]

    color_name = models.CharField(
        choices=CHOICES,
        max_length=6
    )

class Shoe(models.Model):
    size = models.IntegerField()
    brand_name = models.CharField(max_length=25)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=25)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=25)
