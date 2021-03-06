from django.shortcuts import render

from .models import Retailer, Transaction
from user.models import BaseUser
from .serializers import RetailerSerializer, TransactionSerializer

from rest_framework import status, viewsets, permissions
from rest_framework.response import Response


class RetailerVS(viewsets.ModelViewSet):
    queryset = Retailer.objects.all()
    serializer_class = RetailerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = request.headers["auth-token"]
        # keeda kadi with token
        try:
            user = BaseUser.objects.get(contact=token)
        except:
            return Response({'message': 'Invalid Auth Token'},
                            status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                user.retailer
            except:
                # if user.seller is None:
                serializer.save(baseuser=user)
                headers = self.get_success_headers(serializer.data)
                return Response({"message": "Retailer Profile Created!",
                                 "data": serializer.data},
                                status=status.HTTP_201_CREATED,
                                headers=headers)
            else:
                return Response({"message": "Retailer Profile already exists"},
                                status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        token = request.headers["auth-token"]
        try:
            user = BaseUser.objects.get(contact=token)
        except:
            return Response({'message': 'Invalid Auth Token'},
                            status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                retailer = Retailer.objects.get(baseuser=user)
            except:
                return Response({'message': 'User NOT a Retailer'},
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer = self.get_serializer(retailer, data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response({"message": "Data Updated",
                                 "data": serializer.data})

    def destroy(self, request, *args, **kwargs):
        token = request.headers["auth-token"]
        try:
            user = BaseUser.objects.get(contact=token)
        except:
            return Response({'message': 'Invalid Auth Token'},
                            status=status.HTTP_404_NOT_FOUND)
        else:
            print(user.name)
            user.delete()
            return Response({"message": "Deleted Successfully!"},
                            status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        token = request.headers["auth-token"]
        try:
            user = BaseUser.objects.get(contact=token)
        except:
            return Response({'message': 'Invalid Auth Token'},
                            status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                retailer = Retailer.objects.get(baseuser=user)
            except:
                return Response({'message': 'User NOT a Retailer'},
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                print(user.name)
                serializer = self.get_serializer(retailer)
                return Response({"message": "Search Successful!",
                                 "data": serializer.data},
                                status=status.HTTP_200_OK)
