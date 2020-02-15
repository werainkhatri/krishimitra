from django.conf.urls import url, include
from django.urls import path

from . import views

list_rs = views.RetailerVS.as_view({'get': 'list'})
retailer = views.RetailerVS.as_view(
    {'get': 'retrieve',
     'post': 'create',
     'delete': 'destroy',
     'put': 'update'})

urlpatterns = [
    path('list/', list_rs),
    path('', retailer),
]
