from django.shortcuts import render,redirect
from .serializer import ServiceSerializer
from rest_framework import generics
from .models import *
from .forms import *



# class ServiceCreateAPIView(generics.CreateAPIView):
#     queryset               =         Service.objects.all()
#     serializers_class      =         ServiceSerializer
#     permission_classes     =         []
#     authentication_class   =         []

# class ServiceListAPIView(generics.ListAPIView):
#     queryset               =         Service.objects.all()
#     serializers_class      =         ServiceSerializer
#     permission_classes     =         []
#     authentication_class   =         []
    
# class ServiceUpdateAPIView(generics.UpdateAPIView):
#     queryset               =         Service.objects.all()
#     serializers_class      =         ServiceSerializer
#     permission_classes     =         []
#     authentication_class   =         []
#     lookup_field           =         'pk'


