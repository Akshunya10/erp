from django.forms import ModelForm
from django import forms
from .models import *
from services.models import *
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput


class DateInput(forms.DateInput):
    input_type = 'date'


class InvoiceForm(ModelForm):
	class Meta:
		model = Invoice
		fields = ['client_company','Invoice_date','payment_terms','service','description','rate','Qty','Discount','Tax']
		widgets = {'Invoice_date':DateInput()}
        



class PoForm(ModelForm):
  class Meta:
    model=PurchaseOrder
    fields='__all__'
    widgets={'PO_Date':DateInput(),}
    exclude =['Total','PO_Number']

class PEntryForm(ModelForm):
	class Meta:
		model = ServiceEntry
		fields = [
                  'description',
                  'rate',
                  'Qty',
                  'Discount',
                  'Tax']


class ServiceForm(ModelForm):
  class Meta:
    model=Service
    fields='__all__'
    exclude=['name_c','Type','cost']
    

# class PEntryForm(ModelForm):
# 	class Meta:
# 		model = ProductEntry
# 		fields = ['Product',
#                   'description',
#                   'rate',
#                   'Qty',
#                   'Discount',
#                   'Tax']
#         # exclude = []
