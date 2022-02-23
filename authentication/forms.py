from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *
from django.contrib.auth import authenticate


class RegistratinForm(UserCreationForm):
	email=forms.EmailField(max_length=50,help_text='Required. Add a valid email address')
	first_name=forms.CharField(max_length=50)
	class Meta:
		model=User
		fields=("email","first_name","password1","password2",
			'company_create_permission','company_read_permission','company_edit_permission','company_delete_permission',
			'contactperson_create_permission','contactperson_read_permission','contactperson_edit_permission','contactperson_delete_permission',
			'project_create_permission','project_read_permission','project_edit_permission','project_delete_permission','position','department','is_admin')

class userupdateform(forms.ModelForm):
	class Meta:
		model=User
		fields='__all__'
		exclude=['password','is_superuser','is_active','is_staff']
#		fields=("email","first_name",
#                        'company_create_permission','company_read_permission','company_edit_permission','company_delete_permission',
#                        'contactperson_create_permission','contactperson_read_permission','contactperson_edit_permission','contactperson_delete_permission',
#                        'project_create_permission','project_read_permission','project_edit_permission','project_delete_permission','position','department','is_admin')



class UserLoginForm(forms.ModelForm):
	password=forms.CharField(label='Password',widget=forms.PasswordInput)

	class Meta:
		model=User
		fields=('email','password')

	def clean(self):
		if self.is_valid():
			email=self.cleaned_data['email']
			password=self.cleaned_data['password']
			if not authenticate(email=email,password=password):
				raise forms.ValidationError("Invalid Creadentials")


class CompanyCreationForm(forms.ModelForm):
	class Meta:
		model=Company
		fields='__all__'

class PositionForm(forms.ModelForm):
	class Meta:
		model=Position
		fields='__all__'

class ContactPersonCreationForm(forms.ModelForm):
	class Meta:
		model=ContactPerson
		fields='__all__'

class DepartmentForm(forms.ModelForm):
	class Meta:
		model=Department
		fields='__all__'

class BusinessForm(forms.ModelForm):
	class Meta:
		model=Business
		fields='__all__'

class CustomerNewForm(forms.ModelForm):
	class Meta:
		model=CustomerNew
		fields=['company_name']

class VendorNewForm(forms.ModelForm):
	class Meta:
		model=VendorNew
		fields=['company_name']

class CustomerForm(forms.ModelForm):
	class Meta:
		model=Customer
		fields=['first_name','last_name','email_id','contact','address_1','city','state','country','zip_code','customer_id']

# class CustomUserCreationForm(UserCreationForm):

#     class Meta:
#         model = User
#         fields = ('username', 'email','password1','password2')

# class CustomUserChangeForm(UserChangeForm):

#     class Meta:
#         model = User
#         fields = UserChangeForm.Meta.fields


            
        
            
        
