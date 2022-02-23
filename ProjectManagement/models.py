from django.db import models
from django.forms import fields
from django.contrib.auth.models import AbstractUser
from authentication.models import *
import nested_admin
from authentication.models import *
import datetime
stage=[ ('PLANNING','Planning'), ('DEVELOPMENT','Development'),('TESTING','Testing'),
              ('DEPLOYMENT','Deployment'),('COMPLETED','Completed')]

complete_or_Inprogress_choice=[('inprogress','INPROGRESS'),('completed','COMPLETED')]
update=[('allocated','Allocated'),('completed','COMPLETED'),('error','ERROR')]

class Businessopportunity(models.Model):

       project_name       = models.CharField(max_length=100,blank=False,null=False,default='')
       description        = models.TextField(max_length=300,blank=False,null=False)
       company_name       = models.CharField(max_length=100, blank=False, null=False)
       address            = models.CharField(max_length=100, default='')
       contact_person     = models.CharField(max_length=100, blank=False, null=False,default='')
       email_id           = models.EmailField(max_length=100, blank=False, null=False,default='')
       phone_no           = models.CharField(max_length=100,blank=False,null=False,default='')
       additional_contact = models.CharField(max_length=300,blank=False,null='False',default='')
       details            = models.CharField(verbose_name='',max_length=300,blank=False,null='False')
       start_date         = models.DateField()
       deadline           = models.DateField()
       responsible_person = models.ManyToManyField(EmployeeProfile)
       followup_date      = models.DateField()
       followup_message   = models.TextField(max_length=150,default='')
       upload_documents   = models.FileField(blank=True)

       class Meta():
              verbose_name_plural='Business Opportunity'

       def __str__(self):
              return self.company_name

# sa30

# class ProjectDetail(models.Model):
#        project_name=models.CharField(max_length=100,blank=False,null=False)
#        description=models.TextField(max_length=1000, blank=True, null=True)
#        start_date=models.DateField(blank=True)
#        project_deadline=models.DateField(blank=True)
#        company_name=models.CharField(max_length=100,blank=False,null=False)
#        contact_person=models.CharField(max_length=100,blank=True,null=True)
#        project_status=models.CharField(choices=stage, max_length=200, blank=False, null=False)
#        project_complete_or_Inprogress=models.CharField(max_length=20,blank=False,null=False,choices=complete_or_Inprogress_choice)         


# class ProjectTeam(models.Model):
#        project=models.OneToOneField(ProjectDetail,on_delete=models.CASCADE,primary_key=True)
#        project_manager=models.CharField(max_length=50)




# # sa30
class Project(models.Model):
       business           =models.ForeignKey(Business,on_delete=models.CASCADE,blank=True,null=True)

       project_name            =               models.CharField(max_length=100,blank=False,null=False)
       description             =               models.TextField(max_length=100, blank=False, null=False) 
       start_date              =               models.DateField()
       project_deadline        =               models.DateField()
       project_status          =               models.CharField(verbose_name='Project stage',choices=stage, max_length=200, blank=False, null=False, default='')
       project_complete_or_Inprogress=models.CharField(verbose_name='Project status', max_length=20,blank=False,null=False,choices=complete_or_Inprogress_choice)         
       client_company_name     =               models.ForeignKey(Company,on_delete=models.CASCADE)
       # contact_person          =               models.ForeignKey(ContactPerson,on_delete=models.CASCADE)
       responsible_person      =               models.ForeignKey(User,on_delete=models.CASCADE)
       estimate_Price_of_Project  =               models.IntegerField()
       reminder                =               models.DateField()
       reminder_note             =               models.TextField(max_length=100, blank=False, null=False) 
       

       class Meta():
              verbose_name_plural='Project'

       def __str__(self):
              return self.project_name



class Team(models.Model):

       project                 =               models.ForeignKey(Project, on_delete=models.CASCADE,related_name="project_link")
       project_manager=models.ForeignKey(User,on_delete=models.CASCADE)
       team_lead               =               models.ForeignKey(User,related_name='Employee', on_delete=models.CASCADE)

       def __str__(self):
              return self.project.project_name



class TeamMember(models.Model):
       team                    =             models.ForeignKey(Team, on_delete=models.CASCADE,related_name='project_link')
       team_member             =             models.ForeignKey(User, on_delete=models.CASCADE)
       def __str__(self):
              return self.team_member.email

       
class Tasks(models.Model):
       team                    =             models.ForeignKey(Team, on_delete=models.CASCADE,related_name='project_lin')

       
       member                  =               models.ForeignKey(TeamMember, on_delete=models.CASCADE,related_name='member_link')
       task_assigned           =               models.CharField(max_length=100,blank=False,default='')
       updates                  =               models.CharField(max_length=100,choices=update)
       # updates                 =               models.CharField(max_length=100,default='')
       task_deadline           =               models.DateField()
       updated_on              =               models.DateTimeField(default=datetime.datetime.now,blank=True,null=True)
       # class Meta():
       #       verbose_name_plural='Team Member'  
       
       # def __str__(self):
       #        return self.project.project_name








