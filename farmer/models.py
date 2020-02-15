from django.db import models

from user.models import BaseUser


class Farmer(models.Model):
    baseuser = models.OneToOneField(
        BaseUser, related_name='farmer', on_delete=models.CASCADE)
    op_land_area = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.baseuser.name


class Crop(models.Model):
    farmer = models.ForeignKey(
        Farmer, related_name="crop", on_delete=models.CASCADE)
    crop_name = models.CharField(max_length=32)
    crop_type = models.CharField(max_length=32)

    def __str__(self):
        return self.crop_name


class FarmerProduct(models.Model):
    PRODUCT_TYPE = (
        ('CP', 'Crop Product'),
        ('AP', 'Animal Product'),
    )
    PRODUCT_NAME = (
        ('PDY', 'Paddy'),
        ('MZE', 'Maize'),
        ('WHT', 'Wheat'),
        ('JWR', 'Jowar'),
        ('GRN', 'Groundnut'),
        ('GRM', 'Gram'),
        ('RCE', 'Rice'),
        ('BRL', 'Barley'),
    )
    farmer = models.ForeignKey(
        Farmer, related_name="farmer_product", on_delete=models.CASCADE)
    product_name = models.CharField(max_length=32)
    quality_index = models.DecimalField(max_digits=4, decimal_places=2)
    product_type = models.CharField(
        max_length=3, choices=PRODUCT_TYPE, default='CP')

    def __str__(self):
        return self.product_name


class Livestock(models.Model):
    LIVESTOCKS = (
        ('COW', 'COW'),
        ('SHEEP', 'SHEEP'),
        ('GOAT', 'GOAT'),
        ('HEN', 'HEN'),
    )
    farmer = models.ForeignKey(
        Farmer, related_name="livestock", on_delete=models.CASCADE)
    name = models.CharField(max_length=16)
    number = models.IntegerField()

    def __str__(self):
        return self.name
