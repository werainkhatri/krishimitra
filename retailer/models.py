from django.db import models

from user.models import BaseUser


class Retailer(models.Model):
    baseuser = models.OneToOneField(
        BaseUser, related_name='retailer', on_delete=models.CASCADE)
    description = models.CharField(max_length=512)

    def __str__(self):
        return self.baseuser.name


class RetailerProduct(models.Model):
    PRODUCT_TYPE = (
        ('CP', 'Crop Product'),
        ('AP', 'Animal Product'),
    )
    retailer = models.ForeignKey(
        Retailer, related_name='retailer_product', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=32)
    product_price = models.FloatField()
    product_type = models.CharField(
        max_length=3, choices=PRODUCT_TYPE, default='CP')

    def __str__(self):
        return self.product_name
