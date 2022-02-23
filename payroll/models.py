
from django.db import models
from authentication.models import EmployeeProfile,User
    
paymentChoice=[("STRIPE","stripe"),("WORLDPAY","worldpay"),("CHEQUE","cheque"),("BANK_TRANSFER","bank_transfer"),
("CASH","cash")]


class EmployeePackage(models.Model):  # to be send
    # months = (
    #     ('JAN','JAN'),('FEB','FEB'),('MAR','MAR'),('APR','APR'),
    #     ('MAY','MAY'),('JUN','JUN'),('JULY','JULY'),('AUG','AUG'),
    #     ('SEP','SEP'),('OCT','OCT'),('NOV','NOV'),('DEC','DEC'),
    # )

    # Name                  = models.CharField(max_length=20,null=True)
    employee                 = models.ForeignKey(User,on_delete=models.CASCADE,blank=False,null=False)
    # empId                 = models.ForeignKey(EmployeeProfile,on_delete=models.CASCADE,null=True,default = 1)
    # packageId            = models.CharField(max_length=20,null=True)
    # packageId             = models.ForeignKey(SalaryPackage,on_delete=models.CASCADE,null=True,editable=False)
    salary                = models.IntegerField()  # paid_amount
    # salaryMonth     = models.CharField(max_length=20,choices=months,null=True)
    month               =models.CharField(max_length=30,default=" ")
    year                =models.CharField(max_length=10,default=" ")

    date_Of_Payment         = models.DateField()
    # mode_of_payment         = models.CharField(max_length=100,choices=paymentChoice)
    unpaid_leaves_allowed = models.PositiveIntegerField()
    paid_leaves_allowed   = models.PositiveIntegerField()
    comments              = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.employee.email

    class Meta:
        verbose_name_plural = 'employeeSalary'

class MonthlySalary(models.Model):  #dynamic
    # userId          = models.CharField(max_length=20, primary_key=True)
    # EmpId                      = models.ForeignKey(EmployeeProfile,on_delete=models.CASCADE,null=True)
    employee                 = models.ForeignKey(User,on_delete=models.CASCADE,blank=False,null=False)

    month               =models.CharField(max_length=30,default=" ")
    year                =models.CharField(max_length=10,default=" ")

    salary_Month                = models.DateField(null=True)
    # salaryId                   = models.ForeignKey(EmployeePackage, on_delete=models.CASCADE,editable=False,null=True)
    unpaid_leaves              = models.PositiveIntegerField(null=True)
    paid_leaves                = models.PositiveIntegerField(null=True)
    active_Days                 = models.PositiveIntegerField()
    working_Days                = models.PositiveIntegerField()
    mode_of_payment         = models.CharField(max_length=100,choices=paymentChoice)

    # paymentReceipt  = models.ForeignKey(UserPaymentReceipt, on_delete=models.CASCADE)
    total_Salary_Amount        = models.PositiveIntegerField(blank=True,null=True)  # according to no. of days spent

    def __str__(self):
        return self.employee.email

    class Meta:
        verbose_name_plural = 'monthlySalary'
    
    
class Overtime(models.Model):
    employee=models.ForeignKey(User,on_delete=models.CASCADE)
    starttime=models.TimeField(blank=True,null=True)
    endtime=models.TimeField(blank=True,null=True)
    totaltime=models.CharField(max_length=100)
    date=models.DateField(auto_now=False)

    




