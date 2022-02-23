from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from authentication.models import *
from django.db.models.signals import post_save

priority=(('HIGH','High'),
          ('LOW','Low'),
          ('MODERATE','Moderate'))
stage=(('INITIATED','Initiated'),('IN PROGRESS','In Progress'),
       ('RESOLVED','Resolved'))

class SLA(models.Model):

    #owner                   =               models.ForeignKey()

    customer_name           =               models.ManyToManyField(Customer)
    issue                   =               models.CharField(max_length=100,blank='False', null='False')
    priority                =               models.CharField(choices=priority,max_length=200,default='')
    date                    =               models.DateField()
    responsible_person      =               models.ForeignKey(EmployeeProfile,on_delete=models.CASCADE,default='')
    status                  =               models.CharField(choices=stage,max_length=200,null=True)
    solution_details        =               models.CharField(max_length=200,null='True')


    class Meta():
        verbose_name_plural='SLA'

    #def __str__(self):
     #   return ('{}, Ticket no:{}'.format(','.join (self.customer_name.all().values_list('first_name',flat=True)),self.id))
    def __str__(self):
        return ('Ticket no:{},Issue:{}'.format  (self.id,self.issue))


class History(models.Model):

    customer_name                       =               models.ForeignKey(Customer,on_delete=models.CASCADE)
    issue                               =               models.TextField(max_length=300,blank=True)
    ticket_no                           =               models.CharField(max_length=300,blank=True)


    class Meta():
       verbose_name_plural = 'History'
    def __str__(self):
        return str(self.customer_name)

def post_save_history_create_receiver(sender,instance,created,*args, **kwargs):
    a=instance.customer_name_id
    print(a)
    s=SLA.objects.all()
    box=s.filter(customer_name=a)
    print(box)
    i = box.values_list('issue')
    t = box.values_list('id')
    print(i)
    if not instance.issue:
        # l=[]
        # for v in box:
        #     l.append(v)    # not compatible with text field as it is model instance


        # n=len(i)
        #     for c in n:
        #         string =i[n]
        #
        #         print(string)           #str and tpl dont suport + # tuple  immutable so cant add

        #issue  =  i[0]+i[1]+i[2]
        lst =[]
        for vari in i:
                lst.append(vari)
        History.objects.filter(pk=instance.pk).update(issue=lst)
        lst2=[]
        for var in t:
            lst2.append(var)
        History.objects.filter(pk=instance.pk).update(ticket_no=lst2)

post_save.connect(post_save_history_create_receiver, sender=History)



