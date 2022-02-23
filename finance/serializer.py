from rest_framework import serializers
from .models import Invoice,PurchaseOrder

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Invoice
        fields = '__all__'

        # read_only_fields = ['user']



class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model  = PurchaseOrder
        fields = '__all__'



