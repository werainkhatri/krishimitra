from django.db import models

from user.models import BaseUser
from farmer.models import Farmer


class Retailer(models.Model):
    baseuser = models.OneToOneField(
        BaseUser, related_name='retailer', on_delete=models.CASCADE)
    address = models.TextField()
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    pincode = models.CharField(max_length=6, blank=True, null=True)
    lati = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True)
    longi = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.baseuser.name


class Transaction(models.Model):
    buyer = models.ForeignKey(
        BaseUser, related_name='buyer', on_delete=models.CASCADE)
    seller = models.ForeignKey(
        BaseUser, related_name='seller', on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    quantity = models.FloatField()
    price = models.FloatField()

    def __str__(self):
        return str(self.name)+":"+str(self.seller.baseuser.name)+"->"+str(self.buyer.baseuser.name)


# class Rating(models.Model):
#     rated_by = models.ForeignKey(
#         BaseUser, related_name='farmer', on_delete=models.CASCADE)
#     rated_to = models.ForeignKey(
#         BaseUser, related_name='retailer', on_delete=models.CASCADE)
#     rating = models.IntegerField()
#     description = models.TextField(null=True,blank=True)

#     def __str__(self):
#         return str(self.rated_by.name)+"->"+str(self.rated_to.name)
