from rest_framework import serializers
from HR.models import Department,StaffProfile

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Department
        fields = '__all__'


class StaffProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model  = StaffProfile
        fields = '__all__'