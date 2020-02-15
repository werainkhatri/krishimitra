from django.conf.urls import url, include
from django.urls import path

from . import views

list_fs = views.FarmerVS.as_view({'get': 'list'})
farmer = views.FarmerVS.as_view(
    {'get': 'retrieve',
     'post': 'create',
     'delete': 'destroy',
     'put': 'update'})

# list_cs = views.CropVS.as_view({'get': 'list'})
crop = views.CropVS.as_view(
    {'get': 'list',
     'post': 'create'})
crop_edit = views.CropVS.as_view(
    {'delete': 'destroy',
     'put': 'update'})

product = views.ProductVS.as_view(
    {'get': 'list',
     'post': 'create'})
product_edit = views.ProductVS.as_view(
    {'delete': 'destroy',
     'put': 'update'})

ls = views.ProductVS.as_view(
    {'get': 'list',
     'post': 'create'})
ls_edit = views.ProductVS.as_view(
    {'delete': 'destroy',
     'put': 'update'})


urlpatterns = [
    path('list/', list_fs),
    path('', farmer),
    path('crop/<int:pk>/', crop_edit),
    path('crop/', crop),
    path('product/<int:pk>/', product_edit),
    path('product/', product),
    path('ls/<int:pk>/', ls_edit),
    path('ls/', ls),
]
