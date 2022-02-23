from django.shortcuts import render,redirect
from rest_framework import generics,mixins
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication

from .serializer import *
# from rest_framework.decorators import api_view
from services.models import *
from . import views


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



class ServiceListCreateView(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        generics.GenericAPIView):
    queryset                = Service.objects.all()
    serializer_class        = ServiceSerializer
    permission_classes      =   []
    authentication_classes  =   [SessionAuthentication]
    

    def get(self,request,*args,**kwargs):
        return  self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    # def perform_create(self,serializer):
    #     user    = self.request.user
    #     serializer.save(user=user)


class ServiceDetailView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset                = Service.objects.all()
    serializer_class        = ServiceSerializer
    permission_classes      =   []
    authentication_classes  =   [SessionAuthentication]
    lookup_field            = 'pk'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)




class PlanListCreateView(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        generics.GenericAPIView):
    queryset                = Plan.objects.all()
    serializer_class        = PlanSerializer
    permission_classes      =   []
    authentication_classes  =   [SessionAuthentication]


    def get(self,request,*args,**kwargs):
        return  self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


    # def perform_create(self,serializer):
    #     user    = self.request.user
    #     serializer.save(user=user)


class PlanDetailView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset                = Plan.objects.all()
    serializer_class        = PlanSerializer
    permission_classes      =   []
    authentication_classes  =   [SessionAuthentication]
    lookup_field            = 'pk'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)




class ProductListCreateView(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        generics.GenericAPIView):
    queryset                = Product.objects.all()
    serializer_class        = ProductSerializer
    permission_classes      =   []
    authentication_classes  =   [SessionAuthentication]
    

    def get(self,request,*args,**kwargs):
        return  self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


    # def perform_create(self,serializer):
    #     user    = self.request.user
    #     serializer.save(user=user)


class ProductDetailView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset                = Product.objects.all()
    serializer_class        = ProductSerializer
    permission_classes      =   []
    authentication_classes  =   [SessionAuthentication]
    lookup_field            = 'pk'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

