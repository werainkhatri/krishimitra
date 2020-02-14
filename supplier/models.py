from django.db import models
from user.models import BaseUser


class Supplier(models.Model):
    baseuser = models.ForeignKey(
        BaseUser, related_name='supplier', on_delete=models.CASCADE)
    description = models.CharField(max_length=512)

    def __str__(self):
        return self.baseuser.name


class SupplierProduct(models.Model):
    supplier = models.ForeignKey(
        Supplier, related_name='supplier_product', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=32)
    product_price = models.FloatField()

    def __str__(self):
        return self.product_name
