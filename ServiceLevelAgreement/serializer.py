from rest_framework import serializers
from .models import *

class SLASerializer(serializers.ModelSerializer):
      class  Meta:
          model        =           SLA
          fields       =           '__all__'

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
          model         =           History
          fields        =           '__all__'

