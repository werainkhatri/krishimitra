from django.db import models

from user.models import BaseUser


class Farmer(models.Model):
    baseuser = models.OneToOneField(
        BaseUser, related_name='farmer', on_delete=models.CASCADE)
    op_land_area = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)

    address1 = models.CharField(max_length=300, blank=True, null=True)
    address2 = models.CharField(max_length=300, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    pincode = models.CharField(max_length=6, blank=True, null=True)
    lati = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True)
    longi = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True)

    def __str__(self):
        return self.baseuser.name


class Crop(models.Model):
    CROP_TYPE = (
        ('CC', 'Cash Crop'),
        ('FC', 'Food Crop'),
        ('PC', 'Plantation Crop'),
        ('HC', 'Horticulture Crop'),
    )
    farmer = models.ForeignKey(
        Farmer, related_name="crop", on_delete=models.CASCADE)
    crop_name = models.CharField(max_length=32, blank=True, null=True)
    crop_type = models.CharField(max_length=2, choices=CROP_TYPE,
                                 default='CC', blank=True, null=True)

    def __str__(self):
        return self.crop_name


class Product(models.Model):
    PRODUCT_TYPE = (
        ('CP', 'Crop Product'),
        ('AP', 'Animal Product'),
    )
    # PRODUCT_NAME = (
    #     ('PDY', 'Paddy'),
    #     ('MZE', 'Maize'),
    #     ('WHT', 'Wheat'),
    #     ('JWR', 'Jowar'),
    #     ('GRN', 'Groundnut'),
    #     ('GRM', 'Gram'),
    #     ('RCE', 'Rice'),
    #     ('BRL', 'Barley'),
    # )
    farmer = models.ForeignKey(
        Farmer, related_name="product", on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    type = models.CharField(
        max_length=3, choices=PRODUCT_TYPE, default='CP')
    quality_index = models.DecimalField(max_digits=4, decimal_places=2)
    price = models.DecimalField(max_digits=5, decimal_places=0)

    def __str__(self):
        return self.name


class Livestock(models.Model):
    farmer = models.ForeignKey(
        Farmer, related_name="livestock", on_delete=models.CASCADE)
    name = models.CharField(max_length=16)
    amount = models.IntegerField()
    avg_age = models.DecimalField(max_digits=3, decimal_places=0)

    def __str__(self):
        return self.name
