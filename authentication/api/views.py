from django.shortcuts import render,redirect
from django.views import generic
from django.urls import reverse_lazy
from authentication.models import *
from .serializer import LoginSerializer
from django.contrib.auth import authenticate,login,get_user_model
# from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions,authentication
from rest_framework import generics,mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import (
    generics,
    status,
)
from utils.permissions import *
from .serializer import *
# from authentication.renderer import UserJSONRenderer, ClientJSONRenderer
from django.shortcuts import render, get_object_or_404
# from rest_framework.decorators import api_view
from . import views

User = get_user_model()


#
# class RegistrationAPIView(generics.GenericAPIView):
#     """Register new users."""
#     serializer_class = RegistrationSerializer
#     # renderer_classes = (UserJSONRenderer,)
#
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         user_data = serializer.data
#         message = [
#             request,
#             user_data["email"]
#         ]
#
#         response = {
#             "data": {
#                 "user": dict(user_data),
#                 "message": "Account created successfully",
#                 "status": "success"
#             }
#         }
#         return Response(response, status=status.HTTP_201_CREATED)
#
# class LoginAPIView(generics.GenericAPIView):
#     """login a user via email"""
#     serializer_class = LoginSerializer
#     # renderer_classes = (UserJSONRenderer,)
#
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user_data = serializer.data
#         response = {
#             "data": {
#                 "user": dict(user_data),
#                 "message": "You have successfully logged in",
#                 "status": "success"
#             }
#         }
#         return Response(response, status=status.HTTP_200_OK)
# #
class RegistrationAPIView(generics.CreateAPIView):
    authentication_classes      =   []
    permission_classes          =   []
    serializer_class            =   RegisterSerializer
    queryset                    =   User.objects.all()


    def post(self,request,*args,**kwargs):
        if request.method == 'POST':
            serializer = RegisterSerializer(data = request.data)
            data = {}
            if serializer.is_valid():
                user = serializer.save()
                data['response'] = RegisterSerializer.get_message(self,obj=user)
                data['email']    = user.email
                data['username'] = user.username
                data['token']    = RegisterSerializer.get_token(self,obj=user)  # token generation view @
            else:
                data = serializer.errors

            return Response(data)


User=get_user_model()


class LoginAPIView(generics.GenericAPIView):
    authentication_classes      =   []
    permission_classes          =   []
    serializer_class            =   LoginSerializer
    queryset                    =   User.objects.all()


    def post(self,request,*args,**kwargs):
        request             =   self.request
        username            =   request.data['username']
        password            =   request.data['password']
        user                =   authenticate(request,username=username,password=password)
        data = {}
        if user is not None:
            login(request,user)
            serializer = LoginSerializer(data = request.data)
            data['response'] = LoginSerializer.get_message(self,obj=user)
            # response    =   {'messages':'you are logged in ...'}
            data['token']    = LoginSerializer.get_token(self,obj=user)
            # return Response(response)
            return Response(data)

        response    =   {'messages':'invalid credentials'}
        return Response(response)


class RegistrationView(generics.GenericAPIView):
    """Register new users."""
    serializer_class = RegisterSerializer
    # renderer_classes = (UserJSONRenderer,)

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
    """login a user via username"""
    authentication_classes      =   []
    permission_classes          =   []
    serializer_class            =   LoginSerializer
    # queryset                    =   User.objects.all()
    # authentication_classes      =   [authentication.TokenAuthentication]
    permission_classes          =   [permissions.AllowAny]
    

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




class CompanyListCreateView(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        generics.GenericAPIView):
    queryset                = Company.objects.all()
    serializer_class        = CompanySerializer
    permission_classes      =   []
    # authentication_classes  =   [SessionAuthentication]


    def get(self,request,*args,**kwargs):
        return  self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    # def perform_create(self,serializer):
    #     user    = self.request.user
    #     serializer.save(user=user)

class CompanyDetailView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset                = Company.objects.all()
    serializer_class        = CompanySerializer
    permission_classes      = []
    # authentication_classes  = [SessionAuthentication]
    lookup_field            = 'pk'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class EmployeeListCreateView(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        generics.GenericAPIView):
    queryset                = EmployeeProfile.objects.all()
    serializer_class        = EmployeeProfileSerializer
    permission_classes      =   []
    # authentication_classes  =   [SessionAuthentication]


    def get(self,request,*args,**kwargs):
        return  self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


    # def perform_create(self,serializer):
    #     user    = self.request.user
    #     serializer.save(user=user)

class EmployeeDetailView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset                = EmployeeProfile.objects.all()
    serializer_class        = EmployeeProfileSerializer
    permission_classes      = []
    # authentication_classes  = [SessionAuthentication]
    lookup_field            = 'pk'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CustomerListCreateView(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        generics.GenericAPIView):
    queryset                = Customer.objects.all()
    serializer_class        = CustomerSerializer
    permission_classes      =   []
    authentication_classes  =   []


    def get(self,request,*args,**kwargs):
        return  self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


    # def perform_create(self,serializer):
    #     user    = self.request.user
    #     serializer.save(user=user)

class CustomerDetailView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset                = Customer.objects.all()
    serializer_class        = CustomerSerializer
    permission_classes      = []
    authentication_classes  = []
    lookup_field            = 'pk'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)




class VendorListCreateView(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        generics.GenericAPIView):
    queryset                = Vendor.objects.all()
    serializer_class        = VendorSerializer
    permission_classes      =   []
    # authentication_classes  =   [SessionAuthentication]
    

    def get(self,request,*args,**kwargs):
        return  self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
        


    # def perform_create(self,serializer):
    #     user    = self.request.user
    #     serializer.save(user=user)


class VendorDetailView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset                = Vendor.objects.all()
    serializer_class        = VendorSerializer
    permission_classes      = []
    # authentication_classes  = [SessionAuthentication]
    lookup_field            = 'pk'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)





# CUSTOM AUTH API TESTING  - to get the token back with username and password

from rest_framework_jwt.settings import api_settings
from .utils import jwt_response_payload_handler
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class AuthAPI(APIView):
    authentication_classes   = [authentication.SessionAuthentication]
    permission_classes       = [permissions.AllowAny]
    def post(self,request,*args, **kwargs):
        if request.user.is_authenticated:
            return Response({'details':'you are already authenticated'})
        data = request.data
        username = data.get('username')
        print(username)
        password = data.get('password')
        user = authenticate(username = username, password = password)
        print(user)
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload) #creating token manually
        jwt_token = jwt_response_payload_handler(token,user=user,request=request)
        return Response(jwt_token)


# from rest_framework import viewsets
# from .serializer import CustomerSerializer
# from authentication.models import *

# class CustomerViewSet(viewsets.ModelViewSet):
#     serializer_class = CustomerSerializer
#     queryset = Customer.objects.all()
