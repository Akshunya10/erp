# from django.shortcuts import render,redirect
# from .models import Department,StaffProfile
# from .forms import *
# from .serializer import DepartmentSerializer,StaffProfileSerializer
# from rest_framework.generics import (
#     ListAPIView,
#     CreateAPIView,
#     RetrieveAPIView,
#     UpdateAPIView,
#     DestroyAPIView,
# )
#                                         # Department View
# class CreateDepartmentView(CreateAPIView): 
#     queryset = Department.objects.all()
#     serializer_class = DepartmentSerializer

# class ListDepartmentView(ListAPIView):
#     queryset = Department.objects.all()
#     serializer_class = DepartmentSerializer

# class UpdateDepartmentView(UpdateAPIView):
#     queryset         = Department.objects.all()
#     serializer_class = DepartmentSerializer
#     lookup_field     = 'deptId'

                                         
#                                         #  StaffProfile view
# class CreateStaffProfileView(CreateAPIView):
#     queryset                = StaffProfile.objects.all()
#     serializer_class        = StaffProfileSerializer
#     permission_classes      =   []
#     authentication_classes  =   []

# class ListStaffProfileView(ListAPIView):
#     queryset                = StaffProfile.objects.all()
#     serializer_class        = StaffProfileSerializer
#     permission_classes      =   []
#     authentication_classes  =   []

# class UpdateStaffProfileView(UpdateAPIView):
#     queryset                = StaffProfile.objects.all()
#     serializer_class        = StaffProfileSerializer
#     permission_classes      =   []
#     authentication_classes  =   []
#     lookup_field = 'pk'