from django.shortcuts import render,redirect
from .models import Department,StaffProfile
from .forms import *
from .serializer import DepartmentSerializer,StaffProfileSerializer

    


def hr(request):
    return render(request,'hr/dashboard.html')

def hrHome(request):
    return render(request,'hr1/home.html')


def dept(request):
    depts = Department.objects.all()
    context = {'depts':depts}
    return render(request,'hr/dept.html',context)


def deptinfo(request,pk):
    dept = Department.objects.get(id=pk)
    return render(request,'hr/deptinfo.html',{'dept':dept})
    

def createdept(request):
    dept_form = DepartmentForm()
    if request.method == 'POST':
        dept_form = DepartmentForm(request.POST)
        if dept_form.is_valid():
            dept_form.save()

            return redirect('dept')
    
    context = {'dept_form':dept_form}
    return render(request,'hr/dept_form.html',context)


def updatedept(request,pk):  
    dept = Department.objects.get(id=pk)
    dept_form = DepartmentForm(instance=dept)
    if request.method == 'POST':
        dept_form = DepartmentForm(request.POST,instance=dept)
        dept_form.save()

        return redirect('dept')

    context = {'dept_form':dept_form} 
    return render(request,'hr/dept_form.html',context)

def deleteDept(request,pk):
    item = Department.objects.get(id=pk)
    if request.method == 'POST':
        item = Department.objects.get(id=pk)
        item.delete()
        return redirect('dept')

    context = {'item':item}
    return render(request,'hr/deletedept.html',context)



###################################### Below For Staff Views #####################

def staff(request):
    staffs = StaffProfile.objects.all()
    context = {'staffs':staffs}
    return render(request,'hr/staff.html',context)


def staffinfo(request,pk):
    staff = StaffProfile.objects.get(id=pk)
    return render(request,'hr/staffinfo.html',{'staff':staff})

def createstaff(request):
    staff_form = StaffProfileForm()
    if request.method == 'POST':
        staff_form = StaffProfileForm(request.POST)
        if staff_form.is_valid():
            staff_form.save()

            return redirect('staff')
    
    context = {'staff_form':staff_form}
    return render(request,'hr/staff_form.html',context)

def updatestaff(request,pk):  
    staff = StaffProfile.objects.get(id=pk)
    staff_form = StaffProfileForm(instance=staff)
    if request.method == 'POST':
        staff_form = StaffProfileForm(request.POST,instance=staff)
        staff_form.save()

        return redirect('staff')

    context = {'staff_form':staff_form} 
    return render(request,'hr/staff_form.html',context)

def deleteStaff(request,pk):
    item = StaffProfile.objects.get(id=pk)
    if request.method == 'POST':
        item = StaffProfile.objects.get(id=pk)
        item.delete()
        return redirect('staff')

    context = {'item':item}
    return render(request,'hr/deletestaff.html',context)