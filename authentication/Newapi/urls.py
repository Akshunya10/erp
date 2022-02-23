from django.urls import path

from .views import (
    RegistrationAPIView, LoginAPIView,UserListCreateView,UserDetailView
)
from .views import *
# app_name = 'authentication'


urlpatterns = [
    path("register/", RegistrationAPIView.as_view(), name="registerapi"),
    path("login/", LoginAPIView.as_view(), name="login"),

    path('user/', UserListCreateView.as_view(), name='user'),
    path('user/<pk>/', UserDetailView.as_view(), name='user-del'),

   
    # path("logout/", LogoutAPIView.as_view(), name="logout"),
    # path("profile/", ProfileView.as_view(), name="profile"),
]
