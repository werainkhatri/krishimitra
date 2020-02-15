from rest_framework import serializers
from .models import Farmer, Crop, Product, Livestock


class FarmerSerializer(serializers.ModelSerializer):
    baseuser = serializers.ReadOnlyField(source='baseuser.contact')

    class Meta:
        model = Farmer
        read_only_fields = ['id']
        fields = ['id', 'baseuser', 'op_land_area', 'dob', 'address1',
                  'address2', 'city', 'state', 'pincode', 'lati', 'longi']


class CropSerializer(serializers.ModelSerializer):
    farmer = serializers.ReadOnlyField(source='farmer.baseuser.contact')

    class Meta:
        model = Crop
        read_only_fields = ['id']
        fields = ['id', 'farmer', 'crop_name', 'crop_type']


class ProductSerializer(serializers.ModelSerializer):
    farmer = serializers.ReadOnlyField(source='farmer.baseuser.contact')

    class Meta:
        model = Product
        read_only_fields = ['id']
        fields = ['id', 'farmer', 'name', 'type', 'quality_index', 'price']

class LivestockSerializer(serializers.ModelSerializer):
    farmer = serializers.ReadOnlyField(source='farmer.baseuser.contact')

    class Meta:
        model = Livestock
        read_only_fields = ['id']
        fields = ['id', 'farmer', 'name', 'amount', 'avg_age']
