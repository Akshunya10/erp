# from django.shortcuts import render,redirect
# from .forms import * 
# from .models import *
# from .serializer import *
# from rest_framework.generics import (
#     ListAPIView,
#     CreateAPIView,
#     RetrieveAPIView,
#     UpdateAPIView,
#     DestroyAPIView,
# )

#                                                   # UserPaymentReceipt View
# # class CreateUserSalaryPackageView(CreateAPIView): 
# #     queryset                = SalaryPackage.objects.all()
# #     serializer_class        = SalaryPackageSerializer
# #     permission_classes      =   []
# #     authentication_classes  =   []

# # class ListUserSalaryPackageView(ListAPIView):
# #     queryset                = SalaryPackage.objects.all()
# #     serializer_class        = SalaryPackageSerializer
# #     permission_classes      =   []
# #     authentication_classes  =   []

# # class UpdateUserPaymentReceiptView(UpdateAPIView):
# #     queryset                = MonthlySalary.objects.all()
# #     serializer_class        = SalaryPackageSerializer
# #     permission_classes      =   []
# #     authentication_classes  =   []
# #     lookup_field            = 'paymentId'

#                                                       # EmployeePackage view
# class CreateEmployeePackageView(CreateAPIView): 
#     queryset                = EmployeePackage.objects.all()
#     serializer_class        = EmployeePackageSerializer
#     permission_classes      =   []
#     authentication_classes  =   []

# class ListEmployeePackageView(ListAPIView):
#     queryset                = EmployeePackage.objects.all()
#     serializer_class        = EmployeePackageSerializer
#     permission_classes      =   []
#     authentication_classes  =   []

# class UpdateEmployeePackageView(UpdateAPIView):
#     queryset                = EmployeePackage.objects.all()
#     serializer_class        = EmployeePackageSerializer
#     lookup_field = 'pk'
#     permission_classes      =   []
#     authentication_classes  =   []

#                                                        # UserEmployeePaymentBill
# class CreateUserMonthlySalaryView(CreateAPIView): 
#     queryset                = MonthlySalary.objects.all()
#     serializer_class        = MonthlySalarySerializer
#     permission_classes      =   []
#     authentication_classes  =   []

# class ListUserMonthlySalaryView(ListAPIView):
#     queryset                = MonthlySalary.objects.all()
#     serializer_class        = MonthlySalarySerializer
#     permission_classes      =   []
#     authentication_classes  =   []

# class UpdateUserMonthlySalaryBillView(UpdateAPIView):
#     queryset                = MonthlySalary.objects.all()
#     serializer_class        = MonthlySalarySerializer
#     permission_classes      =   []
#     authentication_classes  =   []
#     lookup_field = 'pk'