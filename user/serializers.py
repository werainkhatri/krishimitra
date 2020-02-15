from rest_framework import serializers
from user import models
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError


class SignUpSerializer(serializers.ModelSerializer):

    def save(self, **kwargs):
        self.validated_data['password'] = make_password(
            self.validated_data['password'])
        return super().save(**kwargs)

    class Meta:
        model = models.BaseUser
        read_only_fields = ['id']
        fields = ['id', 'name', 'contact', 'email', 'active',
                  'password']
