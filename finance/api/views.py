from django.shortcuts import render,redirect
from rest_framework import generics,mixins,permissions
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from .serializer import *
# from rest_framework.decorators import api_view
from finance.models import *
# from ServiceEntry.models import  *
from . import views
from utils.permissions import *

from django.contrib.auth.decorators import login_required





class InvoiceListView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()




class PoListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


class PoDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PurchaseOrderSerializer
    queryset = PurchaseOrder.objects.all()




#
# class InvoiceListCreateView(mixins.ListModelMixin,
#                         mixins.CreateModelMixin,
#                         generics.GenericAPIView):
#     queryset                   = Invoice.objects.all()
#     serializer_class           = InvoiceSerializer
#      # permission_classes         =   [permissions.IsAuthenticated,IsOwnerOrReadOnly,IsHR]
#     # authentication_classes    =   [SessionAuthentication]
#     lookup_field = 'pk'
#
#     def get(self,request,*args,**kwargs):
#         return  self.list(request,*args,**kwargs)
#
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)
#
#
#     # def perform_create(self,serializer):
#     #     user= self.request.user
#     #     serializer.save(user=user)
#
#
# class InvoiceDetailView(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset                = Invoice.objects.all()
#     serializer_class        = InvoiceSerializer
#    # permission_classes      = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,permissions.IsAdminUser,IsHR]
#     # authentication_classes  = [SessionAuthentication]
#     lookup_field            = 'pk'
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
#
#     def perform_create(self,serializer):
#         user    = self.request.user
#         serializer.save(user=user)


# class ProductEntryListView(generics.ListCreateAPIView):
#     queryset = ProductEntry.objects.all()
#     serializer_class = ProductEntrySerializer



# class PoListCreateView(mixins.ListModelMixin,
#                         mixins.CreateModelMixin,
#                         generics.GenericAPIView):
#     queryset                = PurchaseOrder.objects.all()
#     serializer_class        = PurchaseOrderSerializer
#    # permission_classes      =  []# [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,IsSuper]
#    #  authentication_classes  =   [SessionAuthentication]
#     #lookup_field = 'pk'

#     def get(self,request,*args,**kwargs):
#         return  self.list(request,*args,**kwargs)

#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)

#     #
#     # def perform_create(self,serializer):
#     #     user    = self.request.user
#     #     serializer.save(user=user)



# class PoDetailView(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset                = PurchaseOrder.objects.all()
#     serializer_class        = PurchaseOrderSerializer
#   #  permission_classes      = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,IsHR]
#     # authentication_classes  = [SessionAuthentication]
#     lookup_field            = 'pk'

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


        
