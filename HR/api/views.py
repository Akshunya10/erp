from django.shortcuts import render,redirect
from rest_framework import generics,mixins
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from .serializer import *
# from rest_framework.decorators import api_view
from HR.models import *
from . import views


class DepartmentListCreateView(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        generics.GenericAPIView):
    queryset                = Department.objects.all()
    serializer_class        = DepartmentSerializer
    permission_classes      =   []
    authentication_classes  =   [SessionAuthentication]
    

    def get(self,request,*args,**kwargs):
        return  self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


    # def perform_create(self,serializer):
    #     user    = self.request.user
    #     serializer.save(user=user)

class DepartmentDetailView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset                = Department.objects.all()
    serializer_class        = DepartmentSerializer
    permission_classes      =   []
    authentication_classes  =   [SessionAuthentication]
    lookup_field            = 'pk'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class StaffProfileListCreateView(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        generics.GenericAPIView):
    queryset                = StaffProfile.objects.all()
    serializer_class        = StaffProfileSerializer
    permission_classes      =   []
    authentication_classes  =   [SessionAuthentication]
    

    def get(self,request,*args,**kwargs):
        return  self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


    # def perform_create(self,serializer):
    #     user    = self.request.user
    #     serializer.save(user=user)


class StaffProfileDetailView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset                = StaffProfile.objects.all()
    serializer_class        = StaffProfileSerializer
    permission_classes      = []
    authentication_classes  = [SessionAuthentication]
    lookup_field            = 'pk'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

