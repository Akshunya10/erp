import jwt
from django.conf import settings
from django.contrib import messages
from django.forms.models import model_to_dict
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from rest_framework import authentication
from rest_framework import permissions,authentication
from rest_framework import generics,mixins
from rest_framework import (
    generics,
    status,
)
from .serializer import *
from rest_framework.exceptions import NotFound
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.views import APIView
# from authentication.models import (User, UserProfile, UserDevices)
from authentication.models import (User)
# from authentication.permissions import (
#     IsClientAdmin,
#     IsProfileOwner,
#     IsOwnerOrAdmin)
from authentication.renderer import UserJSONRenderer, ClientJSONRenderer
from django.core.exceptions import ObjectDoesNotExist
from .serializer import (RegistrationSerializer, LoginSerializer)
from django.core.cache import cache

# from utils import BaseUtils
from utils.permissions import IsViewerOrReadOnly, IsReviewer, IsAdmin
# from utils.emailer import Emailer
from utils.util import generateOTP
# from utils.models import BaseAbstractModel


class RegistrationAPIView(generics.GenericAPIView):
    """Register new users."""
    serializer_class = RegistrationSerializer
    renderer_classes = (UserJSONRenderer,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        message = [
            request,
            user_data["email"]
        ]

        response = {
            "data": {
                "user": dict(user_data),
                "message": "Account created successfully",
                "status": "success"
            }
        }
        return Response(response, status=status.HTTP_201_CREATED)

class LoginAPIView(generics.GenericAPIView):
    """login a user via email"""
    serializer_class = LoginSerializer
    renderer_classes = (UserJSONRenderer,)

    def post(self, request):
        print('now here', request.data)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.data
        response = {
            "data": {
                "user": dict(user_data),
                "message": "You have successfully logged in",
                "status": "success"
            }
        }
        return Response(response, status=status.HTTP_200_OK)



class UserListCreateView(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        generics.GenericAPIView):
    queryset                = User.objects.all()
    serializer_class        = UserSerializer
    permission_classes      =  []
    # authentication_classes  =  [SessionAuthentication]
    lookup_field = 'pk'

    def get(self,request,*args,**kwargs):
        return  self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    # def perform_create(self,serializer):
    #     user    = self.request.user
    #     serializer.save(user=user)

class UserDetailView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset                = User.objects.all()
    serializer_class        = UserSerializer
    permission_classes      = []
    # authentication_classes  = [SessionAuthentication]
    lookup_field            = 'pk'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



