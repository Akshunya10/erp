# from django.shortcuts import render,redirect
# from .models import *
# from django.views import generic
# from django.urls import reverse_lazy
# from .models import User,EmployeeProfile
# from .serializer import LoginSerializer
# from django.contrib.auth import authenticate,login,get_user_model
# from rest_framework import generics
# from rest_framework.response import Response
# from .serializer import UserSerializer,EmployeeProfileSerializer


                                    
# class CreateUserView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes      =   []
#     authentication_classes  =   []

# class ListUserView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes      =   []
#     authentication_classes  =   []

# class UpdateUserView(generics.UpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes      =   []
#     authentication_classes  =   []
#     lookup_field = 'pk'

#                                     # user's profile
# class CreateProfileView(generics.CreateAPIView):
#     queryset = EmployeeProfile.objects.all()
#     serializer_class = EmployeeProfileSerializer
#     permission_classes      =   []
#     authentication_classes  =   []

# class ListProfileView(generics.ListAPIView):
#     queryset = EmployeeProfile.objects.all()
#     serializer_class = EmployeeProfileSerializer
#     permission_classes      =   []
#     authentication_classes  =   []

# class UpdateProfileView(generics.UpdateAPIView):
#     queryset = EmployeeProfile.objects.all()
#     serializer_class = EmployeeProfileSerializer
#     permission_classes      =   []
#     authentication_classes  =   []
#     lookup_field = 'pk'


# User=get_user_model()


# class LoginAPIView(generics.GenericAPIView):
#     authentication_classes      =   []
#     permission_classes          =   []
#     serializer_class            =   LoginSerializer
#     queryset                    =   User.objects.all()


#     def post(self,request,*args,**kwargs):
#         request             =   self.request
#         username            =   request.data['username']
#         password            =   request.data['password']
#         user                =   authenticate(request,username=username,password=password)
#         if user is not None:
#             login(request,user)
#             response    =   {'messages':'you are logged in ...'}
#             return Response(response)
#         response    =   {'messages':'invalid credentials'}
#         return Response(response)