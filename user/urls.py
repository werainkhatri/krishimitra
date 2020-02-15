from django.conf.urls import url, include
from django.urls import path

from . import views


user_post = views.SignUpViewSet.as_view({'post': 'create'})
user_list = views.SignUpViewSet.as_view({'get': 'list'})
user_detail = views.SignUpViewSet.as_view({
    'post':      'update',
    'delete':    'destroy'
})

urlpatterns = [
    path('', user_post),
    path('list/', user_list),
    path('login/', views.login),
    path('update/', user_detail),
]
