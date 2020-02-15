from user.models import BaseUser
from .serializers import BaseUserSerializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout, authenticate

from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, viewsets, permissions
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class BaseUserViewSet(viewsets.ModelViewSet):
    queryset = BaseUser.objects.all()
    serializer_class = BaseUserSerializer

    def update(self, request, *args, **kwargs):
        token = request.headers["auth-token"]
        try:
            user = BaseUser.objects.get(contact=token)
        except:
            return Response({'message': 'Invalid Auth Token', "data": {}},
                            status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = self.get_serializer(user, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "Data Updated",
                             "data": {
                                 'id': serializer.data['id'],
                                 'name': serializer.data['name'],
                                 'contact': serializer.data['contact'],
                                 'email': serializer.data['email'],
                                 'active': serializer.data['active']
                             }})


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    print(request.data)
    contact = request.data.get("contact")
    password = request.data.get("password")
    if contact is None or password is None:
        return Response({'message': 'Contact or Password Missing', 'data': {}},
                        status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(contact=contact, password=password)
    if not user:
        return Response({'message': 'Invalid Credentials', 'data': {}},
                        status=status.HTTP_404_NOT_FOUND)
    # token, s = Token.objects.get_or_create(user=user)
    token = user.contact
    try:
        farmer = user.farmer
    except:
        return Response({"message": "Login Successful",
                         "data": {'token': token,
                                  'user_type': user.user_type,
                                  'contact': user.contact,
                                  'email': user.email,
                                  'name': user.name,
                                  'created_on': user.timestamp,
                                  'superuser': user.is_superuser,
                                  'active': user.active}},
                        status=status.HTTP_200_OK)
    else:
        return Response({"message": "Login Successful",
                         "data": {'token': token,
                                  'user_type': user.user_type,
                                  'contact': user.contact,
                                  'email': user.email,
                                  'name': user.name,
                                  'created_on': user.timestamp,
                                  'superuser': user.is_superuser,
                                  'active': user.active,
                                  'farmer': {"op_land_area": farmer.op_land_area,
                                             "dob": farmer.dob,
                                             "address1": farmer.address1,
                                             "address2": farmer.address2,
                                             "city": farmer.city,
                                             "state": farmer.state,
                                             "pincode": farmer.pincode,
                                             "lati": farmer.lati,
                                             "longi": farmer.longi}
                                  }},
                        status=status.HTTP_200_OK)
