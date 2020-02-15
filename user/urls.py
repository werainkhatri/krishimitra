from django.conf.urls import url, include
from django.urls import path

from . import views


create = views.BaseUserViewSet.as_view({'post': 'create'})
list_all = views.BaseUserViewSet.as_view({'get': 'list'})
update = views.BaseUserViewSet.as_view({'post': 'update'})

urlpatterns = [
    path('', create),
    path('list/', list_all),
    path('login/', views.login),
    path('update/', update),
]
