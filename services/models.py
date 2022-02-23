
from django.db import models
from finance.models import *
from authentication.models import *
from django.conf import settings
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.dispatch import receiver
import random
import string
stage=[ ('initialize','INITIALIZE'), ('inprogress','INPROGRESS'),('solved','SOLVED')]

status=[('inprogress','INPROGRESS'),('solved','SOLVED')]

class Service(models.Model) :
    
 
    
    
    # invoice       = models.ForeignKey(Invoice,on_delete=models.CASCADE,null=True)
    name          = models.CharField(max_length=100,blank=False,null=False)
    serviceId     = models.CharField(max_length=50,null=False,blank=False)
    name_c        = models.CharField(verbose_name='company',max_length=100,blank=False,null=False)
    Type          = models.CharField(verbose_name='Type',max_length=20, blank = True,default='Unknown',null = True)
    # code          = models.CharField(max_length=100)
    description   = models.CharField(max_length=100,blank=True,null=True)
    cost          = models.FloatField(null=True,blank=True)
    rate	=models.FloatField(null=True,blank=True,default=0)
    # Active        = models.BooleanField(default='True')
    quantity	=models.FloatField(null=True,blank=True,default=0)
    discount	=models.FloatField(null=True,blank=True,default=0)
    Tax		=models.FloatField(null=True,blank=True,default=0)    
    
    
    def __str__(self):
        return self.name
    
    

    class Meta:
        verbose_name_plural = 'Service'
        
def random_string_generator(size=7,char=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(char) for _ in range(size))

def serv_id_gen(instance,sender,*args, **kwargs):
    # print(instance.company_code)
    def Letters(*args, **kwargs):
        comp='serv'
        string = str(comp)+"_"+str(instance.name)+"_"+random_string_generator()
        # for i in range(len(instance.first_name)):
        #     if instance.first_name[i] == ' ':
        #         if len(string) == 4:
        #             break
        #         else:
        #             string += instance.first_name[i+1:i+3]
        # # print(self.string)
        return str(string)   

    

    instance.serviceId = Letters() 
    
pre_save.connect(serv_id_gen,sender=Service)


class Plan(models.Model):

    types = (
    ('PREPAID','Prepaid'),
    ('POSTPAID', 'Postpaid'),
    # ('UNKNOWN','Unknown')
    )
    
    planId         = models.CharField(max_length=30,null=True,blank=False)   
    Type           = models.CharField(max_length=20,choices=types,null=True)
    duration       = models.CharField(max_length=20,null = True)
    dateOfCreation = models.DateField(null=True)
    validity       = models.DateField(null=True)
    billingCycle   = models.DateField(null=True)
    dueDate        = models.DateField(null=True)
    terms          = models.TextField(max_length=250,verbose_name='PlanTerms',null=True)

    def __str__(self):
        return self.planId

    class Meta:
        verbose_name_plural = 'plan'
    


class Product(models.Model):
    Product_no          = models.CharField(max_length=30,null=True,blank=False)   
    Product_name        = models.CharField(max_length=20,blank=False,null=True)   
    cost                = models.FloatField()
    # cost                = models.DecimalField(max_digits=20, decimal_places=2, blank=True)
    Company_name        = models.CharField(max_length=20,blank=False)
    Product_Description = models.TextField(max_length=250,null=True)

    def __str__(self):
        return self.Product_name
    
    class Meta:
        verbose_name_plural = 'product'


def prod_no_gen(instance,sender,*args, **kwargs):
    def Letters(*args, **kwargs):
        comp='prod'
        string = str(comp)+"_"+str(instance.Product_name)+"_"+random_string_generator()
 
        return str(string)   

    

    instance.Product_no = Letters() 
    
pre_save.connect(prod_no_gen,sender=Product)

##################################################################################################

                                                            #--------------------FOR SERVICE INLINE



class Complaint(models.Model):
    complaint_by=models.ForeignKey(Customer,on_delete=models.PROTECT)
    ticket_no=models.CharField(max_length=20,blank=True,null=True)
    complaint=models.CharField(max_length=100)
    description=models.TextField(max_length=300)
    complaint_related_to=models.ForeignKey(Service,on_delete=models.PROTECT)
    complaint_handler=models.ForeignKey(User,on_delete=models.PROTECT)
    stage=models.CharField(max_length=50,choices=stage)
    status=models.CharField(max_length=50,choices=status)

    solution=models.TextField(max_length=500,blank=True,null=True)
    created_on=models.DateField(auto_now_add=True)
    updatedAt=models.DateField(auto_now=True)

    def __str__(self):
        return (self.complaint_id)

def pre_save_cust_id(instance,sender,*args,**kwargs):
    # print(instance.company_code)
    def Letters(*args, **kwargs):
        comp='comp'
        string = str(comp)+str(instance.complaint_related_to.serviceId)
        # for i in range(len(instance.first_name)):
        #     if instance.first_name[i] == ' ':
        #         if len(string) == 4:
        #             break
        #         else:
        #             string += instance.first_name[i+1:i+3]
        # # print(self.string)
        return str(string)   

    

    instance.ticket_no = Letters() 
    
pre_save.connect(pre_save_cust_id,sender=Complaint)


