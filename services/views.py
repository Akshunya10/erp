from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.db.models import Q
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.authentication import SessionAuthentication
from .serializer import *


def service(request):
    return render(request,'service/dashboard.html')

def home(request):
    return render(request,'service1/home.html')



####################################################

def plan(request):
    plans = Plan.objects.all()
    context = {'plans':plans}
    return render(request,'service/plan.html',context)


def planinfo(request,pk):
    plan = Plan.objects.get(id=pk)
    return render(request,'service/planinfo.html',{'plan':plan})


def CreatePlan(request):
    plan_form = PlanForm()
    if request.method == 'POST':
        plan_form = PlanForm(request.POST)
        if plan_form.is_valid():
            plan_form.save()

            return redirect('plan')
    
    context = {'plan_form':plan_form}
    return render(request,'service/plan_form.html',context)

def updatePlan(request,pk):  
    plan = Plan.objects.get(id=pk)
    plan_form = PlanForm(instance=plan)
    if request.method == 'POST':
        plan_form = PlanForm(request.POST,instance=plan)
        plan_form.save()

        return redirect('plan')

    context = {'plan_form':plan_form} 
    return render(request,'service/plan_form.html',context)

def deletePlan(request,pk):
    item = Plan.objects.get(id=pk)
    if request.method == 'POST':
        item = Plan.objects.get(id=pk)
        item.delete()
        return redirect('plan')

    context = {'item':item}
    return render(request,'service/deleteplan.html',context)

######################################################

def serv(request):
    services = Service.objects.all()
    context = {'services':services}
    return render(request,'service/service.html',context)


def servinfo(request,pk):
    service = Service.objects.get(id=pk)
    return render(request,'service/servinfo.html',{'service':service})

def CreateService(request):
    context={}
    service_form = ServiceForm()
    services=Service.objects.all()
    context['service_form']=service_form
    context['services']=services
    if request.method == 'POST':
        service_form = ServiceForm(request.POST)
        if service_form.is_valid():
            service_form.save()

            return redirect('createservice')
    
    # context = {'service_form':service_form}
    return render(request,'service/service_form.html',context)

def updateService(request,pk):  
    service = Service.objects.get(id=pk)
    service_form = ServiceForm(instance=service)
    if request.method == 'POST':
        service_form = ServiceForm(request.POST,instance=service)
        service_form.save()

        return redirect('createservice')

    context = {'service_form':service_form} 
    return render(request,'service/service_form.html',context)

def deleteService(request,id):
    if request.user.is_admin:

        pi=Service.objects.get(pk=id)
        pi.delete()
        # messages.success(request,"successful")
        return redirect('createservice')
    else:
        # messages.success(request,"You don't have delete  permission")
        return redirect('createservice')

class ServiceApiView(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Service.objects.all()
    serializer_class=ServiceSerializer
    authentication_classes=[SessionAuthentication]
    
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class UD_ServiceApiView(GenericAPIView,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset=Service.objects.all()
    serializer_class=ServiceSerializer
    authentication_classes=[SessionAuthentication]



    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)


########################################################

def product(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'service/product.html',context)


def prodinfo(request,pk):
    product = Product.objects.get(id=pk)
    return render(request,'service/prodinfo.html',{'product':product})


def CreateProduct(request):
    product_form = ProductForm()
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product_form.save()

            return redirect('prod')
    
    context = {'product_form':product_form}
    return render(request,'service/product_form.html',context)

def updateProduct(request,pk):  
    product = Product.objects.get(id=pk)
    product_form = ProductForm(instance=product)
    if request.method == 'POST':
        product_form = ProductForm(request.POST,instance=product)
        product_form.save()

        return redirect('prod')

    context = {'product_form':product_form} 
    return render(request,'service/product_form.html',context)

def deleteProduct(request,pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item = Product.objects.get(id=pk)
        item.delete()
        return redirect('prod')

    context = {'item':item}
    return render(request,'service/deleteproduct.html',context)

class ComplaintApiView(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Complaint.objects.all()
    serializer_class=ComplaintSerializer
    authentication_classes=[SessionAuthentication]
    
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class UD_ComplaintApiView(GenericAPIView,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset=Complaint.objects.all()
    serializer_class=ComplaintSerializer
    authentication_classes=[SessionAuthentication]



    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)


def complaint(request):
    context={}
    if request.user.is_admin:
        complaint=Complaint.objects.filter(status='inprogress')
        if request.method=="POST":
            form=ComplaintForm(request.POST)
            if form.is_valid():
                form.save()
                context['complaint']=complaint
                return redirect('complaint')

            else:
                context['complaint']=complaint
                context['form']=form
        else:
            form=ComplaintForm()
            context['form']=form
            context['complaint']=complaint
        return render(request,'service1/complaint.html',context)
    else:
        return redirect('userlogin')

def complaintdb(request):
    context={}

    if request.user.is_admin:
        query=" "
        if request.GET:
            query=request.GET['q']
            context['query']=str(query)

            complaint=Complaint.objects.filter(Q(complaint_by__first_name=query) | Q(complaint_by__first_name__icontains=query) | Q(complaint_handler__firstname=query)| Q(complaint_handler__firstname__icontains=query) | Q(ticket_no=query) | Q(ticket_no__icontains=query) |Q(complaint_related_to__name=query) | Q(complaint_related_to__name__icontains=query) | Q(description__icontains=query))

            context['complaint']=complaint
            return render(request,'service1/complaintdb.html',context)

 

        complaint=Complaint.objects.all()
        context['complaint']=complaint
        return render(request,'service1/complaintdb.html',context)
    else:
        return redirect('userlogin')


def complaintdelete(request,id):
    if request.user.is_admin:

        pi=Complaint.objects.get(pk=id)
        pi.delete()
        # messages.success(request,"successful")
        return redirect('complaint')
    else:
        # messages.success(request,"You don't have delete contact person permission")
        return redirect('complaint')

def complaintview(request,id):
    complaint=Complaint.objects.get(pk=id)
    context={}
    context['complaint']=complaint
    return render(request,'service/complaintdes.html',context)

def complaintupdate(request,id):

    if request.method=="POST":
        pi=Complaint.objects.get(pk=id)
        form=ComplaintForm(request.POST,instance=pi)
        if form.is_valid():
            form.save()
            # messages.success(request,"successful")
            return redirect('complaint')

    pi=Complaint.objects.get(pk=id)
    form=ComplaintForm(instance=pi)
    return render(request,'service1/complaint.html',{'form':form})





    