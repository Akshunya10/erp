from django import forms
from .models import *


stage=[ ('PLANNING','Planning'), ('DEVELOPMENT','Development'),('TESTING','Testing'),
              ('DEPLOYMENT','Deployment'),('COMPLETED','Completed')]

complete_or_Inprogress_choice=[('inprogress','INPROGRESS'),('completed','COMPLETED')]

class DateInput(forms.DateInput):
	input_type='date'

class ProjectCreationForm(forms.ModelForm):
	class Meta:
		model=Project
		fields='__all__'
		widgets={
		'start_date':DateInput(),
		'project_deadline':DateInput(),
		'reminder':DateInput()
		}
		# widgets={
		# 'project_name':forms.TextInput(attrs={'class':'form-control'}),
		# 'description':forms.TextInput(attrs={'class':'form-control ',}),
		# 'start_date':forms.TextInput(attrs={'class':'form-control'}),
		# 'project_deadline':forms.TextInput(attrs={'class':'form-control'}),
		# 'client_company_name':forms.TextInput(attrs={'class':'form-control'}),
		# 'contact_person':forms.TextInput(attrs={'class':'form-control'}),
		# # 'project_status':forms.TextInput(attrs={'class':'form-control'}),
		# # 'project_complete_or_Inprogress':forms.TextInput(attrs={'class':'form-control'})
		# }


class TeamCreationForm(forms.ModelForm):
	class Meta:
		model=Team
		fields='__all__'
		# widgets={
		# 'project_name':forms.TextInput(attrs={'class':'form-control'}),
		# 'description':forms.TextInput(attrs={'class':'form-control ',}),
		# 'start_date':forms.TextInput(attrs={'class':'form-control'}),
		# 'project_deadline':forms.TextInput(attrs={'class':'form-control'}),
		# 'client_company_name':forms.TextInput(attrs={'class':'form-control'}),
		# 'contact_person':forms.TextInput(attrs={'class':'form-control'})
		# # 'project_status':forms.ChoiceField(attrs={'class':'form-control'}),
		# # 'project_complete_or_Inprogress':forms.TextInput(attrs={'class':'form-control'})
		# }


class TeamMemberCreationForm(forms.ModelForm):
	class Meta:
		model=TeamMember
		fields='__all__'

class AllocateTaskForm(forms.ModelForm):
	class Meta:
		model=Tasks
		fields='__all__'
		widgets={
		# 'member':forms.TextInput(attrs={'class':'form-control'}),
		# 'task_assigned':forms.TextInput(attrs={'class':'form-control ',}),
		# 'updates':forms.TextInput(attrs={'class':'form-control'}),
		'task_deadline':DateInput(),
		
		}	


class Addtaskinfopage(forms.ModelForm):
	class Meta:
		model=Tasks
		fields='__all__'
		exclude=['team','member']
		widgets={
		# 'member':forms.TextInput(attrs={'class':'form-control'}),
		# 'task_assigned':forms.TextInput(attrs={'class':'form-control ',}),
		# 'updates':forms.TextInput(attrs={'class':'form-control'}),
		'task_deadline':DateInput(),
		# 'task_deadline':forms.TextInput(attrs={'class':'form-control'}),
		
		}		








