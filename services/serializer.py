from .models import *
from rest_framework import serializers

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        
        model   = Service
        fields  = '__all__'

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model=Complaint 
        fields='__all__'

