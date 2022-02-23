from django.forms import ModelForm
from .models import *
from django import forms
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput


class DateInput(forms.DateInput):
    input_type = 'date'
	
class TimeInput(forms.TimeInput):
	input_type="time"

class PackageForm(ModelForm):
	class Meta:
		model = EmployeePackage
		fields = '__all__'
		widgets = {
            
            'date_Of_Payment': DateInput(),
            
        }
		exclude = ['salary_Month']


class MonthlySalForm(ModelForm):
	class Meta:
		model = MonthlySalary
		fields = '__all__'
		widgets = {
            
            'salary_Month': DateInput(),
            
        }
		exclude = ['salary_Month','total_Salary_Amount']

class OvertimeForm(ModelForm):
	class Meta:
		model = Overtime
		fields = '__all__'
		widgets = {
            
            # 'starttime': TimeInput(),
			# 'endtime' : TimeInput(),
			'date' :DateInput()
            
        }
		exclude = ['starttime','endtime']
