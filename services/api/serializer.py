from services.models import *
from rest_framework import serializers

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:                    # if class meta is not defined then give 'str object has no attribute value' error.
        model   = Service
        fields  = '__all__'

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Plan
        fields  = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Product
        fields  = '__all__'