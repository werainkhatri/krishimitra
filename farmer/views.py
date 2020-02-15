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
        data = request.data
        # return Response(data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = request.headers["auth-token"]
        # keeda kadi with token
        user = BaseUser.objects.get(contact=token)
        try:
            farmer = user.farmer
        except:
            # if user.seller is None:
            user.active = 0
            print(user.active)
            serializer.save(baseuser=user)
            # print(serializer.data.baseuser.active)
            headers = self.get_success_headers(serializer.data)
            return Response({"message": "Farmer Profile Created!", "data": serializer.data}, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({"message": "Farmer Profile already exists"})

    def update(self, request, *args, **kwargs):
        token = request.headers["auth-token"]
        try:
            user = BaseUser.objects.get(contact=token)
        except:
            return Response({'message': 'Invalid Auth Token'},
                            status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                farmer = Farmer.objects.get(baseuser=user)
            except:
                return Response({'message': 'User NOT a Farmer'},
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer = self.get_serializer(farmer, data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response({"message": "Data Updated", "data": serializer.data})
