from user.models import BaseUser as User
from .serializers import SignUpSerializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout, authenticate

from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, viewsets, permissions
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class SignUpViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    contact = request.data.get("contact")
    password = request.data.get("password")
    if contact is None or password is None:
        return Response({'error': 'Contact or Password Missing'},
                        status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(contact=contact, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=status.HTTP_404_NOT_FOUND)
    # token, s = Token.objects.get_or_create(user=user)
    token = user.contact
    # try:
    #     seller = user.seller
    # except:
    return Response({'token': token,
                     'user_type': user.user_type,
                     'contact': user.contact,
                     'email': user.email,
                     'full_name': user.name,
                     'timestamp': user.timestamp,
                     'superuser': user.is_superuser,
                     'active': user.active},
                    status=status.HTTP_200_OK)
    # else:
    #     return Response({'token': token,
    #                      'contact': user.contact,
    #                      'email': user.email,
    #                      'full_name': user.full_name,
    #                      'active': user.active,
    #                      'timestamp': user.timestamp,
    #                      'role': user.role,
    #                      "seller": {"store_name": seller.store_name,
    #                                 "legal_name": seller.legal_name,
    #                                 "address1": seller.address1,
    #                                 "address2": seller.address2,
    #                                 "city": seller.city,
    #                                 "state": seller.state,
    #                                 "pincode": seller.pincode,
    #                                 "lati": seller.lati,
    #                                 "longi": seller.longi,
    #                                 "gstin": seller.gstin,
    #                                 "pan": seller.pan,
    #                                 "acc_holder_name": seller.acc_holder_name,
    #                                 "acc_type": seller.acc_type,
    #                                 "acc_number": seller.acc_number,
    #                                 "ifsc_code": seller.ifsc_code}
    #                      },
    #                     status=status.HTTP_200_OK)
