from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from services.models import *
from .serializer import InvoiceSerializer,PurchaseOrderSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework import generics,mixins
from services.models import *
from .forms import *
from .filters import *
from django.db.models.signals import pre_save,post_save
from django.db.models import Q
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.authentication import SessionAuthentication
from .serializer import *
from payroll.models import *

# Import PDF Stuff
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


# PurchaseOrderSerializer
# MonthlySalary
class InvoiceApiView(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Invoice.objects.all()
    serializer_class=InvoiceSerializer
    authentication_classes=[SessionAuthentication]
    
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class UD_InvoiceApiView(GenericAPIView,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset=Invoice.objects.all()
    serializer_class=InvoiceSerializer
    authentication_classes=[SessionAuthentication]



    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

class PoApiView(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=PurchaseOrder.objects.all()
    serializer_class=PurchaseOrderSerializer
    authentication_classes=[SessionAuthentication]
    
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class UD_PoApiView(GenericAPIView,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset=PurchaseOrder.objects.all()
    serializer_class=PurchaseOrderSerializer
    authentication_classes=[SessionAuthentication]



    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)



def financeHome(request):
    return render(request,'finance1/home.html')


def finance(request):
    return render(request,'finance/dashboard.html')


def invoice(request):
    context={}
    query=" "
    if request.GET:
        query=request.GET['q']
        context['query']=str(query)
        invoices=Invoice.objects.filter(Q(client_company__company_name=query)| Q(client_company__company_name__icontains=query) |Q(payment_terms=query) | Q(payment_terms__icontains=query)).order_by('client_company__company_name')


        context['invoices']=invoices 
        return render(request,'finance/invoice.html',context)

    invoices=Invoice.objects.all().order_by('client_company__company_name')

    context['invoices']=invoices
 
   

    return render(request,'finance/invoice.html',context)

# def invoice(request):
#     context={}
#     query=" "
#     if request.GET:

#         query=request.GET['q']
#         context['query']=str(query)
#         invoices=Invoice.objects.filter(Q(client_company__company_Name=query) | Q(client_company__company_Name__icontains=query) | Q(Invoice_number=query)| Q(Invoice_number__icontains=query  | Q(payment_terms=query) | Q(payment_terms__icontains=query))

#         context['invoices']=invoices
#         return render(request,'finance/invoice.html',context)

#     invoices = Invoice.objects.all()
#     context['invoices']=invoices
   

#     return render(request,'finance/invoice.html',context)

    # invfilter = InvoiceFilter(request.GET,queryset=invoices)
    # invoices = invfilter.qs

    # context = {'invoices':invoices,}
    # context = {'invoices': invoices, 'invfilter': invfilter}
    # return render(request,'finance/invoice.html',context)


def invinfo(request,pk):
    invoice = Invoice.objects.get(id=pk)
    # entries = invoice.serviceentry_set.all()
    # s = 0
    # for q in entries.iterator():         ############## need to modify , its wrong here
    #     s += (q.rate * q.Qty) - (((q.Discount)/100) * (q.Qty * q.rate)) + q.Tax
    
    
    # context = {'invoice':invoice,'entries':entries} #,'sum': s
    context = {'invoice':invoice} #,'sum': s
    return render(request,'finance/invinfo.html',context)

def createinvoice(request):
    inv_form = InvoiceForm() 
    service_form=ServiceForm()
   
    # ent_form = SEntryForm()
    if request.method == 'POST':
        inv_form = InvoiceForm(request.POST)
        service_form=ServiceForm(request.POST)

        if inv_form.is_valid():
            #pre_save.send(sender=Invoice)
            inv_form.save()
            #pre_save.send(sender=Invoice)
            return redirect('invoices')

        # print("inv_form  :" ,inv_form)
        # ent_form = SEntryForm(request.POST)
        # if inv_form.is_valid() and ent_form.is_valid():

        # if inv_form.is_valid() and service_form.is_valid():
        #     service=service_form.save()
        #     invoice=inv_form.save(commit=False)
        #     invoice.service=service
        #     invoice.save()
        # if inv_form.is_valid():
            # inv = inv_form.save()
            # inv.pre_save.connect(pre_save_Stotal, sender=Invoice)
            # ent = ent_form.save(commit=False)


            # ent.invoice = inv
            # ent.save()
        if service_form.is_valid():
            service_form.save()
                # pre_save.send(sender=Invoice)
            return redirect('create_invoice')



    # context = {'inv_form':inv_form,'ent_form':ent_form}
    context = {'inv_form':inv_form,'service_form':service_form}

    return render(request,'finance/invoice_form.html',context)


def updateinvoice(request,pk): # only for updating the invoice,
    invoice = Invoice.objects.get(id=pk)
    # entry = ServiceEntry.objects.get(id=pk)
    inv_form = InvoiceForm(instance=invoice)
    # ent_form = SEntryForm(instance=entry)
    if request.method == 'POST':
        inv_form = InvoiceForm(request.POST,instance=invoice)
        # ent_form = SEntryForm(request.POST,instance=entry)
        if inv_form.is_valid(): #and ent_form.is_valid():
            inv = inv_form.save()
            # ent = ent_form.save(False)

            # ent.invoice = inv
            # ent.save()
            return redirect('invoices')
    context = {'inv_form':inv_form} #,'ent_form':ent_form
    
    return render(request,'finance/updinv_form.html',context)

# Generate a PDF File Venue List
def invoice_pdf(request,pk):
	# Create Bytestream buffer
    buf = io.BytesIO()
	# Create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
	# Create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)
	
	# Designate The Model
    invoice = Invoice.objects.get(id=pk)

	# Create blank list
    lines = []
    lines.append("Details")
    lines.append("-------------------------------------------")
    lines.append("Invoice No   :{} ".format(str(invoice.Invoice_number)))
    lines.append("Company Name :{} ".format(str(invoice.client_company.company_name)))
    lines.append("Date         :{} ".format(str(invoice.Invoice_date)))
    lines.append("Payment Term :{} ".format(str(invoice.payment_terms)))
    lines.append("--------------------------------------------")
    lines.append("Service Name :{} ".format(str(invoice.service.name)))
    lines.append("Description  :{} ".format(str(invoice.description)))
    lines.append("Quantity     :{} ".format(str(invoice.Qty)))
    lines.append("Rate         :{} ".format(str(invoice.rate)))
    lines.append("Discount     :{} ".format(str(invoice.Discount)))
    lines.append("Tax          :{} ".format(str(invoice.Tax)))
    lines.append("----------------------------------------------")
    lines.append("Total        :{} ".format(str(invoice.Total)))
	# Loop
    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

	# Return something
    return FileResponse(buf,as_attachment=True,filename='invoice.pdf')



def updateSEnt(request,pk):  # SERVICE ENTRY
    entry = ServiceEntry.objects.get(id=pk)
    ent_form = SEntryForm(instance=entry)
    if request.method == 'POST':
        ent_form = SEntryForm(request.POST,instance=entry)
        ent = ent_form.save()

        return redirect('invoice')

    context = {'ent_form':ent_form} #,'ent_form':ent_form
    return render(request,'finance/updinvent_form.html',context)


def deleteinvoice(request,pk):
    item = Invoice.objects.get(id=pk)
    if request.method == 'POST':
        item = Invoice.objects.get(id=pk)
        item.delete()
        return redirect('invoices')

    context = {'item':item}
    return render(request,'finance/deleteinv.html',context)

def deleteSEnt(request,pk):
    item = ServiceEntry.objects.get(id=pk)
    # obj = Invoice.objects.get(id=pk)
    if request.method == 'POST':
        item = ServiceEntry.objects.get(id=pk)
        item.delete()
        # obj = Invoice.objects.get(id=pk)
        return redirect('invoice')

    context = {'item':item}
    return render(request,'finance/deleteinv.html',context)



############################################# Below PURCHASE ORDER VIEWS ####################################


# def po(request):
#     pos = PurchaseOrder.objects.all()
#     context = {'pos':pos}
#     return render(request,'finance/po.html',context)

def po(request):
    context={}
    query=" "
    if request.GET:
        query=request.GET['q']
        context['query']=str(query)
        pos=PurchaseOrder.objects.filter(Q(Vendor__company_name=query)| Q(Vendor__company_name__icontains=query) ).order_by('Vendor__company_name')


        context['pos']=pos 
        return render(request,'finance/po.html',context)

    pos=PurchaseOrder.objects.all().order_by('Vendor__company_name')

    context['pos']=pos
 
   

    return render(request,'finance/po.html',context)



def poinfo(request,pk):
    po = PurchaseOrder.objects.get(id=pk)
    # entries = po.productentry_set.all()
    # s = 0
    # for q in entries.iterator():
    #     s += (q.rate * q.Qty) - (((q.Discount)/100) * (q.Qty * q.rate)) + q.Tax

    context = {'po':po,}
    # context = {'po':po,'entries':entries,'sum': s}
    return render(request,'finance/poinfo.html',context)

def po_pdf(request,pk):
	# Create Bytestream buffer
    buf = io.BytesIO()
	# Create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
	# Create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)
	
	# Designate The Model
    invoice = PurchaseOrder.objects.get(id=pk)

	# Create blank list
    lines = []
    lines.append("Details")
    lines.append("-------------------------------------------")
    lines.append("PO No             :   {} ".format(str(invoice.PO_Number)))
    lines.append("Vendor Name       :   {} ".format(str(invoice.Vendor.company_name)))
    lines.append("Date              :   {} ".format(str(invoice.PO_Date)))
    # lines.append("Payment Term :{} ".format(str(invoice.payment_terms)))
    lines.append("--------------------------------------------")
    lines.append("Service Name      :   {} ".format(str(invoice.service.name)))
    lines.append("Description       :   {} ".format(str(invoice.description)))
    lines.append("Quantity          :   {} ".format(str(invoice.Qty)))
    lines.append("Rate              :   {} ".format(str(invoice.rate)))
    lines.append("Discount          :   {} ".format(str(invoice.Discount)))
    lines.append("Tax               :   {} ".format(str(invoice.Tax)))
    lines.append("----------------------------------------------")
    lines.append("Total             :   {} ".format(str(invoice.Total)))
	# Loop
    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

	# Return something
    return FileResponse(buf,as_attachment=True,filename='po.pdf')




def createPO(request):
    po_form = PoForm()
    service_form=ServiceForm()
    # ent_form = PEntryForm()

   
    # ent_form = SEntryForm()
    if request.method == 'POST':
        inv_form = PoForm(request.POST)
        service_form=ServiceForm(request.POST)
        
        if inv_form.is_valid():
            inv_form.save()
            # pre_save.send(sender=Invoice)
            return redirect('poS')

        if service_form.is_valid():
            service_form.save()
            return redirect('create_po')
    # if request.method == 'POST':
    #     po_form = PoForm(request.POST)
    #     service_form=ServiceForm(request.POST)
    #     # ent_form = PEntryForm(request.POST)
    #     if service_form.is_valid():
    #         service_form.save()
    #         return redirect('create_po')

    #     if po_form.is_valid():
    #     # if po_form.is_valid() and ent_form.is_valid():
    #         po = po_form.save()
            # ent = ent_form.save(False)

            # ent.PO = po
            # ent.save()
            # return redirect('poS')

    # context = {'po_form':po_form,'ent_form':ent_form}
    context = {'po_form':po_form,'service_form':service_form}

    return render(request,'finance/po_form.html',context)


def updatePO(request,pk): # only for updating the invoice, for service entry create another view 
    po = PurchaseOrder.objects.get(id=pk)
    po_form = PoForm(instance=po)
    if request.method == 'POST':
        po_form = PoForm(request.POST,instance=po)
        if po_form.is_valid(): 
            po = po_form.save()
            
            return redirect('poS')
    context = {'po_form':po_form} 
    
    return render(request,'finance/updpo_form.html',context)


def updatePEnt(request,pk):  # PRODUCT ENTRY
    entry = ProductEntry.objects.get(id=pk)
    ent_form = PEntryForm(instance=entry)
    if request.method == 'POST':
        ent_form = PEntryForm(request.POST,instance=entry)
        ent = ent_form.save()

        return redirect('po')

    context = {'ent_form':ent_form} #,'ent_form':ent_form
    
    return render(request,'finance/updpoent_form.html',context)


def deletePO(request,pk):
    item = PurchaseOrder.objects.get(id=pk)
    if request.method == 'POST':
        item = PurchaseOrder.objects.get(id=pk)
        item.delete()
        return redirect('poS')

    context = {'item':item}
    return render(request,'finance/deletepo.html',context)

def deletePEnt(request,pk):
    item = ProductEntry.objects.get(id=pk)
    # obj = Invoice.objects.get(id=pk)
    if request.method == 'POST':
        item = ProductEntry.objects.get(id=pk)
        item.delete()
        # obj = Invoice.objects.get(id=pk)
        return redirect('po')

    context = {'item':item}
    return render(request,'finance/deletepo.html',context)


def receipts(request):
    context = {}
    data = ReceiptEn.objects.all()
    context['data'] = data
    
    if request.method == "POST":
        d = request.POST.get('dt')
        pr = request.POST.get('par')
        dr = request.POST.get('dr')
        cr = request.POST.get('cr')
#        print("#####################",d,pr,dr,cr)
        re = ReceiptEn.objects.create(particular=pr, date=d, debit=dr, credit=cr)
        re.save()
        return redirect('/finance/receipts')
    return render(request,'finance/receipts.html', context)
    
def payments(request):
    data = PaymentEn.objects.all()
    if request.method == "POST":
        d = request.POST.get('dt')
        pr = request.POST.get('par')
        dr = request.POST.get('dr')
        cr = request.POST.get('cr')
#        print(d,pr,dr,cr)
        re = PaymentEn.objects.create(particular=pr, date=d, debit=dr, credit=cr)
        re.save()
        return redirect('/finance/payment')
    return render(request,'finance/payment.html',{'data':data})
    
def contra(request):
    data = ContraEn.objects.all()
    if request.method == "POST":
        d = request.POST.get('dt')
        pr = request.POST.get('par')
        dr = request.POST.get('dr')
        cr = request.POST.get('cr')
#        print(d,pr,dr,cr)
        re = ContraEn.objects.create(particular=pr, date=d, debit=dr, credit=cr)
        re.save()
        return redirect('/finance/contra')
    return render(request,'finance/contra.html',{'data':data})
    
def journal(request):
    context = {}
    data = JournalEn.objects.all()    
    context['data'] = data

    if request.method == "POST":
        d = request.POST.get('dt')
        pr = request.POST.get('par')
        dr = request.POST.get('dr')
        cr = request.POST.get('cr')
#        print(d,pr,dr,cr)
        re = JournalEn.objects.create(particular=pr, date=d, debit=dr, credit=cr)
        re.save()    
        return redirect('/finance/journal') 
    return render(request,'finance/journal.html', context)

def ledgercreation(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        dep = request.POST.get('dep')
#        print(name,amount,dep)
        led = Ledger.objects.create(name=name,amount=amount,dep=dep)     
        led.save()   

    details = Ledger.objects.all()
 #   print(details)
    return render(request, 'finance/ledger.html',{'data':details})
    
def profit_loss(request):
    context = {}
    # po = PurchaseOrder.objects.all()
    invo = Invoice.objects.all()

    isum =0
    for j in invo:
        isum += j.Total
    context['invo'] = isum

    pay = MonthlySalary.objects.all()
    psum = 0
    for k in pay:
        psum += k.total_Salary_Amount 
    context['pay'] = round(psum)

    j = JournalEn.objects.all()      
    p = PaymentEn.objects.all()       
    c = ContraEn.objects.all()        
    r = ReceiptEn.objects.all().order_by('-date') 
    list = sorted(chain(j,p,c,r), key=lambda instance: instance.date) 
        # print(context)
    d = 0
    c = 0 
    for i in list:
        if i.credit:
            c=c+i.credit
        else:
            d=d+i.debit

    context['expenditure'] = round(d + isum)
    context['earning'] = round(c)

    res = round(c-(d+isum+psum))
    if res > 0:
        context['profit'] = res
    else:
        context['loss'] = res

    print(context)
    return render(request, 'finance/profit.html', context)

from itertools import chain
def balance_sheet(request):
    context = {}
    if request.method=='POST':
        sdt = request.POST.get('sdt')
        edt = request.POST.get('edt')
        # print(sdt,edt)
        j = JournalEn.objects.filter(date__range=(sdt,edt)).order_by('-date')       
        p = PaymentEn.objects.filter(date__range=(sdt,edt)).order_by('-date')       
        c = ContraEn.objects.filter(date__range=(sdt,edt)).order_by('-date')        
        r = ReceiptEn.objects.filter(date__range=(sdt,edt)).order_by('-date')     

        list = sorted(chain(j,p,c,r), key=lambda instance: instance.date)
        p = 0
        p1=[]
        
        for i in list:
            if i.credit:
                p=p+i.credit
                p1.append(p)
            else:
                p=p-i.debit
                p1.append(p)
        
        p1  = p1 
        mylist = zip(list, p1)
        context = {'mylist':mylist,}
        
    else:
        j = JournalEn.objects.all().order_by('-date')       
        p = PaymentEn.objects.all().order_by('-date')       
        c = ContraEn.objects.all().order_by('-date')        
        r = ReceiptEn.objects.all().order_by('-date') 
        list = sorted(chain(j,p,c,r), key=lambda instance: instance.date) 
        # print(context)
        p = 0
        p1=[]
        
        for i in list:
            if i.credit:
                p=p+i.credit
                p1.append(p)
            else:
                p=p-i.debit
                p1.append(p)
        
        p1  = p1 
        mylist = zip(list, p1)
        context = {'mylist':mylist,}
         
    return render(request, 'finance/balancesheet.html', context)



def ledger_delete(request, pk):
    
    Ledger.objects.filter(id=pk).delete() 
    return redirect('/finance/ledger/')


def updateledger(request,pk):
    context ={}
    id = Ledger.objects.get(id=pk)
    print(id)
    context['data']= id
    if request.method == 'POST':
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        dep = request.POST.get('dep')
        
        data1 = Ledger.objects.get(id=pk)
        data1.name = name 
        data1.amount = amount 
        data1.dep = dep 
        data1.save()

        return redirect('/finance/ledger/')
    return render(request, 'finance/editledger.html', context)

def journaldelete(request, pk):    
    JournalEn.objects.filter(id=pk).delete() 
    return redirect('/finance/journal/')


def updatejournal(request, pk):
    context ={}
    id = JournalEn.objects.filter(id=pk)
    print('_______________',id)
    context['data']= id
    if request.method == 'POST':
        dt = request.POST.get('dt')
        par = request.POST.get('par')
        dr = request.POST.get('dr')
        cr = request.POST.get('cr')
        
        data1 = JournalEn.objects.get(id=pk)
        data1.date = dt
        data1.particular = par
        data1.debit = dr 
        data1.credit = cr
        data1.save()
        return redirect('/finance/journal/')
    return render(request, 'finance/editjournal.html', context) 


def receiptdelete(request, pk):    
    ReceiptEn.objects.filter(id=pk).delete() 
    return redirect('/finance/receipts/')

def updatereceipt(request, pk):
    context={}
    data = ReceiptEn.objects.filter(id=pk)
    context['data'] = data
    if request.method == 'POST':
        dt = request.POST.get('dt')
        par = request.POST.get('par')
        dr = request.POST.get('dr')
        cr = request.POST.get('cr')
        
        data1 = ReceiptEn.objects.get(id=pk)
        data1.date = dt
        data1.particular = par
        data1.debit = dr 
        data1.credit = cr
        data1.save()
        return redirect('/finance/receipts/')

    return render(request, 'finance/editreceipts.html', context) 


def paymentdelete(request, pk):    
    PaymentEn.objects.filter(id=pk).delete() 
    return redirect('/finance/payment/')

def updatepayment(request, pk):
    context={}
    data = PaymentEn.objects.filter(id=pk)
    context['data'] = data
    if request.method == 'POST':
        dt = request.POST.get('dt')
        par = request.POST.get('par')
        dr = request.POST.get('dr')
        cr = request.POST.get('cr')
        
        data1 = PaymentEn.objects.get(id=pk)
        data1.date = dt
        data1.particular = par
        data1.debit = dr 
        data1.credit = cr
        data1.save()
        return redirect('/finance/payment/') 
        
    return render(request, 'finance/editpayment.html', context)
 

def contradelete(request, pk):    
    ContraEn.objects.filter(id=pk).delete() 
    return redirect('/finance/contra/')

def updatecontra(request, pk):
    context={}
    data = ContraEn.objects.filter(id=pk)
    context['data'] = data
    if request.method == 'POST':
        dt = request.POST.get('dt')
        par = request.POST.get('par')
        dr = request.POST.get('dr')
        cr = request.POST.get('cr')
        
        data1 = ContraEn.objects.get(id=pk)
        data1.date = dt
        data1.particular = par
        data1.debit = dr 
        data1.credit = cr
        data1.save()
        return redirect('/finance/contra/')
        
    return render(request, 'finance/editcontra.html', context) 



