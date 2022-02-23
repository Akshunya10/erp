from rest_framework import serializers
from payroll.models import *

# class SalaryPackageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model  = SalaryPackage
#         fields = '__all__'


class EmployeePackageSerializer(serializers.ModelSerializer):
    class Meta:
        model  = EmployeePackage
        fields = '__all__'


class MonthlySalarySerializer(serializers.ModelSerializer):
    class Meta:
        model  = MonthlySalary
        fields = '__all__'



