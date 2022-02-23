from django.forms import ModelForm
from django import forms
from .models import *
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput



class DateInput(forms.DateInput):
    input_type = 'date'

class PlanForm(ModelForm):
	class Meta:
		model = Plan
		fields = '__all__'
		widgets = {
            
            'dateOfCreation': DateInput(),
            'validity'      : DateInput(),
            'billingCycle'  : DateInput(),
            'dueDate'       : DateInput(),
        }
		#exclude = []

        
class ServiceForm(ModelForm):
	class Meta:
		model = Service
		fields = '__all__'
		#fields = ('name', 'serviceId','description','rate','discount')
		widgets = {
            
            'dateOfPayment': DateInput(),
            
        }
		exclude = ['name_c','Type','cost','quantity','Tax','serviceId']


class ProductForm(ModelForm):
	class Meta:
		model = Product
		fields = '__all__'
		widgets = {
            
            'salaryMonth': DateInput(),
            
        }
		exclude = ['Company_name','Product_no']

class ComplaintForm(ModelForm):
    class Meta:
        model=Complaint
        fields='__all__'
        exclude=['ticket_no']
       



