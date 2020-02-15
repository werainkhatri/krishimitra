from django.conf.urls import url, include
from django.urls import path

from . import views

list_all = views.FarmerVS.as_view({'get': 'list'})
add = views.FarmerVS.as_view({'post': 'create'})
update = views.FarmerVS.as_view({'post': 'update'})

urlpatterns = [
    path('list/', list_all),
    path('', add),
    path('update/', update),
]
