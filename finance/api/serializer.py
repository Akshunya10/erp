from rest_framework import serializers,fields
from finance.models import Invoice,PurchaseOrder


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Invoice
        fields = '__all__'

# class InvoiceSerializer(serializers.ModelSerializer):


#     invoice_link= ServiceEntrySerializer (many=True)

#     class Meta:
#         model  = Invoice
#         fields = ['from_company','customer_name','Invoice_number','Invoice_date','payment_terms','Total','invoice_link']
#         read_only_fields = ['user']


#     def create(self, validated_data):
#         invoice_services = validated_data.pop('invoice_link')
#         invoice = Invoice.objects.create(**validated_data)
#         for invoice_service in invoice_services:
#             ServiceEntry.objects.create(invoice=invoice, **invoice_service)
#         return invoice

   

#     def update(self, instance, validated_data):
#         invoice_services= validated_data.pop('invoice_link')
#         serviceEntries = (instance.invoice_link).all()
#         serviceEntries = list(serviceEntries)
#         instance.from_company = validated_data.get('from_company', instance.from_company)
#         instance.customer_name = validated_data.get('customer_name', instance.customer_name)
#         instance.Invoice_number = validated_data.get('Invoice_number', instance.Invoice_number)
#         instance.Invoice_date = validated_data.get('Invoice_date', instance.Invoice_date)
#         instance.payment_terms = validated_data.get('payment_terms', instance.payment_terms)
#         instance.Total = validated_data.get('Total', instance.Total)
#         instance.save()

#         for invoice_service in invoice_services:
#             serviceEntry = serviceEntries.pop(0)
#             serviceEntry.service = invoice_service.get('service', serviceEntry.service)
#             serviceEntry.description = invoice_service.get('description', serviceEntry.description)
#             serviceEntry.rate = invoice_service.get('rate', serviceEntry.rate)
#             serviceEntry.Qty = invoice_service.get('Qty', serviceEntry.Qty)
#             serviceEntry.Discount = invoice_service.get('Discount', serviceEntry.Discount)
#             serviceEntry.Tax = invoice_service.get('Tax', serviceEntry.Tax)
#             serviceEntry.save()
#         return instance


# # -------------------------------------------------------------------- Product--------------------

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model  = PurchaseOrder
        fields = '__all__'

# class PurchaseOrderSerializer(serializers.ModelSerializer):
#     product_link = ProductEntrySerializer( many=True)
#     class Meta:
#         model  = PurchaseOrder
#         fields = ['from_company','vendor_name','PO_Number','PO_Date','Total','product_link']
#         read_only_fields = ['user']


#     def create(self, validated_data):
#         po_products = validated_data.pop('product_link')
#         poObject = PurchaseOrder.objects.create(**validated_data)
#         for po_product in po_products:
#             ProductEntry.objects.create(PO=poObject, **po_product)
#         return poObject

#     def update(self, instance, validated_data):
#         po_products= validated_data.pop('product_link')
#         productEntries = (instance.product_link).all()
#         productEntries = list(productEntries)
#         instance.Vendor = validated_data.get('Vendor', instance.Vendor)
#         instance.from_company = validated_data.get('from_company', instance.from_company)
#         instance.vendor_name = validated_data.get('vendor_name', instance.vendor_name)
#         instance.PO_Number = validated_data.get('PO_Number', instance.PO_Number)
#         instance.PO_Date = validated_data.get('PO_Date', instance.PO_Date)
#         instance.Total = validated_data.get('Total', instance.Total)
#         instance.save()

#         for po_product in po_products:
#             productEntry = productEntries.pop(0)
#             productEntry.Product = po_product.get('Product', productEntry.Product)
#             productEntry.description = po_product.get('description', productEntry.description)
#             productEntry.rate = po_product.get('rate', productEntry.rate)
#             productEntry.Qty = po_product.get('Qty', productEntry.Qty)
#             productEntry.Discount = po_product.get('Discount', productEntry.Discount)
#             productEntry.Tax = po_product.get('Tax', productEntry.Tax)

#             productEntry.save()
#         return instance
