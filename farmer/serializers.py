from rest_framework import serializers
from .models import Farmer
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError


class FarmerSerializer(serializers.ModelSerializer):
    baseuser = serializers.ReadOnlyField(source='baseuser.contact')

    class Meta:
        model = Farmer
        read_only_fields = ['id']
        fields = ['id', 'baseuser', 'op_land_area', 'dob', 'address1',
                  'address2', 'city', 'state', 'pincode', 'lati', 'longi']
