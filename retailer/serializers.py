from rest_framework import serializers
from .models import Retailer, Transaction


class RetailerSerializer(serializers.ModelSerializer):
    baseuser = serializers.ReadOnlyField(source='baseuser.contact')

    class Meta:
        model = Retailer
        read_only_fields = ['id']
        fields = ['id', 'baseuser', 'address', 'city',
                  'state', 'pincode', 'lati', 'longi', 'description']


class TransactionSerializer(serializers.ModelSerializer):
    buyer = serializers.ReadOnlyField(source='buyer.contact')
    seller = serializers.ReadOnlyField(source='seller.contact')

    class Meta:
        model = Transaction
        read_only_fields = ['id']
        fields = ['id', 'buyer', 'seller', 'name',
                  'quantity', 'price']
