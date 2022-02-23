from django.shortcuts import render,redirect
from .forms import * 
from .models import *
from django.db.models import Q
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.authentication import SessionAuthentication
from .serializer import *
# Import PDF Stuff
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


# MonthlySalarySerializer
# MonthlySalary
class EmployeepackageApiView(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=EmployeePackage.objects.all()
    serializer_class=EmployeePackageSerializer
    authentication_classes=[SessionAuthentication]
    
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class UD_EmployeepackageApiView(GenericAPIView,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset=EmployeePackage.objects.all()
    serializer_class=EmployeePackageSerializer
    authentication_classes=[SessionAuthentication]



    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

class MonthlysalaryApiView(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=MonthlySalary.objects.all()
    serializer_class=MonthlySalarySerializer
    authentication_classes=[SessionAuthentication]
    
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class UD_MonthlysalaryApiView(GenericAPIView,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset=MonthlySalary.objects.all()
    serializer_class=MonthlySalarySerializer
    authentication_classes=[SessionAuthentication]



    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

def payroll(request):
    return render(request,'payroll/dashboard.html')

def payrollHome(request):
    return render(request,'payroll1/home.html')
    
def empsalary(request):
    context={}
    query=" "
    if request.GET:
        query=request.GET['q']
        context['query']=str(query)
        packages=EmployeePackage.objects.filter(Q(employee__email=query)| Q(employee__email__icontains=query) |Q(employee__department__department_name__icontains=query)).order_by('employee__firstname')


        context['packages']=packages 
        return render(request,'payroll/empsalary.html',context)

    packages=EmployeePackage.objects.all().order_by('employee__firstname')

    context['packages']=packages
 
   

    return render(request,'payroll/empsalary.html',context)
    # packages = EmployeePackage.objects.all()
    # context = {'packages':packages}


def empsalinfo(request,pk):
    package = EmployeePackage.objects.get(id=pk)
    return render(request,'payroll/empsalinfo.html',{'package':package})


def createEmpPac(request): # empPack is empsalary; both naming are alike
    pack_form = PackageForm()
    if request.method == 'POST':
        pack_form = PackageForm(request.POST)
        if pack_form.is_valid():
            pack_form.save()

            return redirect('empsal')

    context = {'pack_form':pack_form}

    return render(request,'payroll/empsal_form.html',context)

def updatePack(request,pk):  
    pack = EmployeePackage.objects.get(id=pk)
    pack_form = PackageForm(instance=pack)
    if request.method == 'POST':
        pack_form = PackageForm(request.POST,instance=pack)
        pack_form.save()

        return redirect('empsal')

    context = {'pack_form':pack_form} 
    return render(request,'payroll/empsal_form.html',context)


def deletePack(request,pk):
    item = EmployeePackage.objects.get(id=pk)
    if request.method == 'POST':
        item = EmployeePackage.objects.get(id=pk)
        item.delete()
        return redirect('empsal')

    context = {'item':item}
    return render(request,'payroll/deletesal.html',context)


################################################### Below MonthlySalary Views ##################################

def monthsal(request):
    context={}
    query=" "
    if request.GET:
        query=request.GET['q']
        context['query']=str(query)
        salaries=MonthlySalary.objects.filter(Q(employee__email=query)| Q(employee__email__icontains=query) |Q(mode_of_payment=query) | Q(mode_of_payment__icontains=query) | Q(employee__department__department_name__icontains=query)).order_by('employee__firstname')


        context['salaries']=salaries 
        return render(request,'payroll/monthsal.html',context)

    salaries=MonthlySalary.objects.all().order_by('employee__firstname')
    context['salaries']=salaries
    return render(request,'payroll/monthsal.html',context)

    # salaries = MonthlySalary.objects.all()
    # context = {'salaries':salaries}


def monthsalinfo(request,pk):
    salary = MonthlySalary.objects.get(id=pk)
    return render(request,'payroll/monthsalinfo.html',{'salary':salary})

# Generate a PDF File Venue List
def monthsal_pdf(request,pk):
	# Create Bytestream buffer
    buf = io.BytesIO()
	# Create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
	# Create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)
	
	# Designate The Model
    invoice = MonthlySalary.objects.get(id=pk)

	# Create blank list
    lines = []
    lines.append("Details")
    lines.append("-------------------------------------------")
    lines.append("Name              :{} ".format(str(invoice.employee.firstname)))
    lines.append("Email             :{} ".format(str(invoice.employee.email)))
   
    lines.append("Mode of payment   :{} ".format(str(invoice.mode_of_payment)))
    lines.append("Paid leaves       :{} ".format(str(invoice.paid_leaves)))
    lines.append("Unpaid leaves     :{} ".format(str(invoice.unpaid_leaves)))
    lines.append("Active days       :{} ".format(str(invoice.active_Days)))
    lines.append("Salary month      :{} ".format(str(invoice.month)))
    lines.append("Salary year       :{} ".format(str(invoice.year)))

    lines.append("Working days      :{} ".format(str(invoice.working_Days)))
    lines.append("----------------------------------------------")
    lines.append("Amount            :{} ".format(str(invoice.total_Salary_Amount)))
	# Loop
    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

	# Return something
    return FileResponse(buf,as_attachment=True,filename='monthsal.pdf')



def createovertime(request):
    form=OvertimeForm()
    context={}
    context['form']=form
    if request.method == "POST" :
        form=OvertimeForm(request.POST)
        # start=request.POST['starttime']
        # end=request.POST['endtime']
        
        # print('start',start)
        if form.is_valid():
            form.save()
            return redirect('monthsala')
    return render(request,'payroll/createovertime.html',context)

def createMonthSal(request): #
    monthsal_form = MonthlySalForm()
    overtimerate=100
    if request.method == 'POST':

        monthsal_form = MonthlySalForm(request.POST)
        paid_leave=request.POST['paid_leaves']
        unpaid_leave=request.POST['unpaid_leaves']
        activedays=request.POST['active_Days']
        workingdays=request.POST['working_Days']
        print(paid_leave)
        employe=request.POST['employee']
        salarypackage=EmployeePackage.objects.filter(employee=employe).first()
        print(employe)
        overtime=Overtime.objects.filter(employee=employe).values('totaltime')
        print(overtime)
        alltime=0
        extra_pay=0
        if overtime:
            for i in overtime:
                alltime=alltime+int(i['totaltime'])
            extra_pay=float(alltime/60)*overtimerate
            print(alltime)
            print(extra_pay)
        print(salarypackage)
        print('salary',salarypackage.salary)
        perday=int(salarypackage.salary)/int(workingdays)
        monsal=(int(activedays)*int(perday)-int(unpaid_leave)*int(perday))+extra_pay
        print('monthsal',monsal)
        if monthsal_form.is_valid():
            x=monthsal_form.save(commit=False)
            x.total_Salary_Amount=monsal
            x.save()
            return redirect('monthsala')

    context = {'monthsal_form':monthsal_form}

    return render(request,'payroll/monthsal_form.html',context)

def updateMonthSal(request,pk):  
    sal = MonthlySalary.objects.get(id=pk)
    monthsal_form = MonthlySalForm(instance=sal)
    if request.method == 'POST':
        monthsal_form = MonthlySalForm(request.POST,instance=sal)
        monthsal_form.save()

        return redirect('monthsala')

    context = {'monthsal_form':monthsal_form} 
    return render(request,'payroll/monthsal_form.html',context)


def deleteMonthSal(request,pk):
    item = MonthlySalary.objects.get(id=pk)
    if request.method == 'POST':
        item = MonthlySalary.objects.get(id=pk)
        item.delete()
        return redirect('monthsala')

    context = {'item':item}
    return render(request,'payroll/deletemonthsal.html',context)
