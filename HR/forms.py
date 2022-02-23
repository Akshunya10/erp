from django.forms import ModelForm,forms
from .models import *
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput


class DepartmentForm(ModelForm):
	class Meta:
		model = Department
		fields = '__all__'
		
    


class StaffProfileForm(ModelForm):
	class Meta:
		model = StaffProfile
		fields = '__all__'
        # widgets = {

        #     'Joining_date': DatePickerInput()

        # }
        
        


