from django.shortcuts import render,redirect
from rest_framework import generics,mixins
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from .serializer import *
# from rest_framework.decorators import api_view
from payroll.models import *
from . import views


class EmployeePackageListCreateView(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        generics.GenericAPIView):
    queryset                = EmployeePackage.objects.all()
    serializer_class        = EmployeePackageSerializer
    permission_classes      =   []
    authentication_classes  =   [SessionAuthentication]


    def get(self,request,*args,**kwargs):
        return  self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


    

    # def perform_create(self,serializer):
    #     user    = self.request.user
    #     serializer.save(user=user)


class EmployeePackageDetailView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = EmployeePackage.objects.all()
    serializer_class = EmployeePackageSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class MonthlySalaryListCreateView(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        generics.GenericAPIView):
    queryset                = MonthlySalary.objects.all()
    serializer_class        = MonthlySalarySerializer
    permission_classes      =   []
    authentication_classes  =   [SessionAuthentication]
    

    def get(self,request,*args,**kwargs):
        return  self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


    # def perform_create(self,serializer):
    #     user    = self.request.user
    #     serializer.save(user=user)



class MonthlySalaryDetailView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset                = MonthlySalary.objects.all()
    serializer_class        = MonthlySalarySerializer
    permission_classes      =   []
    authentication_classes  =   [SessionAuthentication]
    lookup_field            = 'pk'
 
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)