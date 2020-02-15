from django.shortcuts import render

from .models import Farmer
from user.models import BaseUser
from .serializers import FarmerSerializer

from rest_framework import status, viewsets, permissions
from rest_framework.response import Response

class FarmerVS(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = request.headers["auth-token"]
        # keeda kadi with token
        user = BaseUser.objects.get(contact=token)
        try:
            farmer = user.farmer
        except:
            # if user.seller is None:
            print(user.active)
            serializer.save(baseuser=user)
            headers = self.get_success_headers(serializer.data)
            return Response({"data": serializer.data}, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({"message": "Farmer Profile already exists"})

    
    