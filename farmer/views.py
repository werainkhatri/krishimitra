from django.shortcuts import render

from .models import Farmer, Crop, Product, Livestock
from user.models import BaseUser
from .serializers import FarmerSerializer, CropSerializer, ProductSerializer, LivestockSerializer

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
        try:
            user = BaseUser.objects.get(contact=token)
        except:
            return Response({'message': 'Invalid Auth Token'},
                            status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                user.farmer
            except:
                # if user.seller is None:
                serializer.save(baseuser=user)
                headers = self.get_success_headers(serializer.data)
                return Response({"message": "Farmer Profile Created!",
                                 "data": serializer.data},
                                status=status.HTTP_201_CREATED,
                                headers=headers)
            else:
                return Response({"message": "Farmer Profile already exists"},
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
                farmer = Farmer.objects.get(baseuser=user)
            except:
                return Response({'message': 'User NOT a Farmer'},
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer = self.get_serializer(farmer, data=request.data)
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
                farmer = Farmer.objects.get(baseuser=user)
            except:
                return Response({'message': 'User NOT a Farmer'},
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                print(user.name)
                serializer = self.get_serializer(farmer)
                return Response({"message": "Search Successful!",
                                 "data": serializer.data},
                                status=status.HTTP_200_OK)


class CropVS(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer

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
                farmer = Farmer.objects.get(baseuser=user)
            except:
                return Response({'message': 'User NOT a Farmer'},
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save(farmer=farmer)
                headers = self.get_success_headers(serializer.data)
                return Response({"message": "Crop Added Successfully",
                                 "data": serializer.data},
                                status=status.HTTP_201_CREATED,
                                headers=headers)

    def list(self, request, *args, **kwargs):
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
                queryset = Crop.objects.filter(farmer=farmer)

                page = self.paginate_queryset(queryset)
                if page is not None:
                    serializer = self.get_serializer(page, many=True)
                    return self.get_paginated_response({"message": "Success!",
                                                        "data": serializer.data})

                serializer = self.get_serializer(queryset, many=True)
                return Response({"message": "Success!",
                                 "data": serializer.data},
                                status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "Deleted Entry Successfully!"},
                        status=status.HTTP_204_NO_CONTENT)


class ProductVS(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

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
                farmer = Farmer.objects.get(baseuser=user)
            except:
                return Response({'message': 'User NOT a Farmer'},
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save(farmer=farmer)
                headers = self.get_success_headers(serializer.data)
                return Response({"message": "Product Added Successfully",
                                 "data": serializer.data},
                                status=status.HTTP_201_CREATED,
                                headers=headers)

    def list(self, request, *args, **kwargs):
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
                queryset = Product.objects.filter(farmer=farmer)

                page = self.paginate_queryset(queryset)
                if page is not None:
                    serializer = self.get_serializer(page, many=True)
                    return self.get_paginated_response({"message": "Success!",
                                                        "data": serializer.data})

                serializer = self.get_serializer(queryset, many=True)
                return Response({"message": "Success!",
                                 "data": serializer.data},
                                status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "Deleted Entry Successfully!"},
                        status=status.HTTP_204_NO_CONTENT)


class LivestockVS(viewsets.ModelViewSet):
    queryset = Livestock.objects.all()
    serializer_class = LivestockSerializer

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
                farmer = Farmer.objects.get(baseuser=user)
            except:
                return Response({'message': 'User NOT a Farmer'},
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save(farmer=farmer)
                headers = self.get_success_headers(serializer.data)
                return Response({"message": "Livestock Added Successfully",
                                 "data": serializer.data},
                                status=status.HTTP_201_CREATED,
                                headers=headers)

    def list(self, request, *args, **kwargs):
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
                queryset = Livestock.objects.filter(farmer=farmer)

                page = self.paginate_queryset(queryset)
                if page is not None:
                    serializer = self.get_serializer(page, many=True)
                    return self.get_paginated_response({"message": "Success!",
                                                        "data": serializer.data})

                serializer = self.get_serializer(queryset, many=True)
                return Response({"message": "Success!",
                                 "data": serializer.data},
                                status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "Deleted Entry Successfully!"},
                        status=status.HTTP_204_NO_CONTENT)
