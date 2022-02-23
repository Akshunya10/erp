from django.forms.models import construct_instance
from django.shortcuts import render,redirect

from .models import * 
from .forms import *

# Import PDF Stuff
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
# Create your views here.
def creatematerial(request):
    form=MaterialForm()
    context={}
    context['form']=form
    material=Material.objects.all()
    context['material']=material
    if request.method == "POST" :
        form=MaterialForm(request.POST)

        # start=request.POST['starttime']
        # end=request.POST['endtime']
        
        # print('start',start)
        if form.is_valid():
            form.save()
            context[material]=Material.objects.all()
            return redirect('creatematerial')

    return render(request,'production/materialdata.html',context)


# def materialinfo(request,pk):
#     material = Material.objects.get(id=pk)
#     return render(request,'production/materialinfo.html',{'material':material})


def updatematerial(request,pk):  
    material = Material.objects.get(pk=pk)
    form = MaterialForm(instance=material)
    if request.method == 'POST':
        form = MaterialForm(request.POST,instance=material)
        form.save()

        return redirect('creatematerial')

    context = {'form':form} 
    return render(request,'production/materialdata.html',context)

def deletematerial(request,id):
    if request.user.is_admin:

        pi=Material.objects.get(pk=id)
        pi.delete()
        # messages.success(request,"successful")
        return redirect('creatematerial')
    else:
        # messages.success(request,"You don't have delete  permission")
        return redirect('creatematerial')

def createProductmat(request):
    form=ProductmatForm()
    context={}
    context['form']=form
    if request.method == "POST" :
        form=ProductmatForm(request.POST)
        # start=request.POST['starttime']
        # end=request.POST['endtime']
        
        # print('start',start)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userdashboard')

    return render(request,'production/createProductmat.html',context)

def createProductmat(request):
    productmat_form = ProductmatForm()
    mat=Productwithqty.objects.filter(active=True)

    # productmat_form.fields["material"].queryset = Productwithqty.objects.filter(active=True) 
    prodwithqty_form=ProdwithQtyForm()
   
    # ent_form = SEntryForm()
    if request.method == 'POST':
        productmat_form = ProductmatForm(request.POST)
        prodwithqty_form=ProdwithQtyForm(request.POST)

        if productmat_form.is_valid():
            mat=Productwithqty.objects.filter(active=True)
            p=productmat_form.save(commit=False)
            pname=productmat_form.cleaned_data['product_name']
            pq=1
            
            item=ProductionMaterial()
            item.product_name=pname
            item.produced_quantity=pq
            item.save()
            prodmat=ProductionMaterial.objects.filter(product_name=pname).first()
            try:
                obj = Stock.objects.get(item__product_name=pname)
                print('existing stock',float(obj.quantity))
                obj.quantity = float(obj.quantity)+float(pq)
                print('qt',pq)
                print('new obj.qt',obj.quantity)

                # print('existing stock',float(obj.quantity)+float(qty))
                obj.save()
            except Stock.DoesNotExist:
                print(pq)
                b=Stock.objects.create(item=prodmat,quantity=pq)

                b.save()
            for x in mat:
                item.material.add(x)
                item.save()
                inv=Inventory.objects.filter(available_item__name= x.item.name).first()
                inv.quantity=float(inv.quantity)-float(x.quantity)
                print('update invent',float(inv.quantity)-float(x.quantity))
                inv.save()
                x.active=False
                x.save()

            return redirect('stockdata')
        if prodwithqty_form.is_valid():

            prodwithqty_form.save()
            return redirect('createproductmat')



    # context = {'inv_form':inv_form,'ent_form':ent_form}
    context = {'productmat_form':productmat_form,'prodwithqty_form':prodwithqty_form,'mat':mat}

    return render(request,'production/createProductmat.html',context)


def productmatdata(request):
    context={}
    productmat=ProductionMaterial.objects.all()
    context['productmat']=productmat
    return render(request,'production/productmatdata.html',context)

def productmatinfo(request,id=None):
    context={}
    productmat=ProductionMaterial.objects.filter(pk=id).first()
    context['productmat']=productmat
    return render(request,'production/productmatinfo.html',context)


def updateproductmat(request,pk):  

    pack = ProductionMaterial.objects.get(id=pk)
    prodwithqty_form=ProdwithQtyForm(request.POST)

    productmat_form = ProductmatForm(instance=pack)
    productmat_form.fields["material"].queryset = Productwithqty.objects.filter(active=True) 
    if request.method == 'POST':
        productmat_form = ProductmatForm(request.POST,instance=pack)
        productmat_form.save()
    if request.method == 'POST':
        productmat_form = ProductmatForm(request.POST,instance=pack)
        prodwithqty_form=ProdwithQtyForm(request.POST)

        if productmat_form.is_valid():

            p=productmat_form.save(commit=False)
            if 'material' in productmat_form.cleaned_data:
                print(productmat_form.cleaned_data['material'])
                for a in productmat_form.cleaned_data['material']:
                    inv=Inventory.objects.filter(available_item__name=a.item).first()
                    inv.quantity=float(inv.quantity)-float(a.quantity)
                    print('update invent',float(inv.quantity)-float(a.quantity))
                    inv.save()
                    a.active=False
                    a.save()
                p.save()
            return redirect('userdashboard')
        if prodwithqty_form.is_valid():

            prodwithqty_form.save()
            return redirect('createproductmat')


        return redirect('productmatdata')
    context = {'productmat_form':productmat_form,'prodwithqty_form':prodwithqty_form}

    # context = {'productmat_form':productmat_form} 
    return render(request,'production/createProductmat.html',context)

def deleteproductmat(request,id):
    if request.user.is_admin:

        pi=ProductionMaterial.objects.get(pk=id)
        pi.delete()
        return redirect('productmatdata')
    else:
        return redirect('productmatdata')

def createstock(request):
    form=StockForm()
    context={}
    context['form']=form
    
    if request.method == "POST" :
        form=StockForm(request.POST)

        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stockdata')

    return render(request,'production/createstock.html',context)

def stockdata(request):
    context={}
    stock=Stock.objects.all()
    context['stock']=stock
    return render(request,'production/stockdata.html',context)

def stockinfo(request,id=None):
    context={}
    stock=Stock.objects.filter(pk=id).first()
    context['stock']=stock
    return render(request,'production/stockinfo.html',context)


def updatestock(request,pk):  
    pack = Stock.objects.get(id=pk)
    form = StockForm(instance=pack)
    if request.method == 'POST':
        form = StockForm(request.POST,instance=pack)
        form.save()

        return redirect('stockdata')

    context = {'form':form} 
    return render(request,'production/createstock.html',context)

def deletestock(request,id):
    if request.user.is_admin:

        pi=Stock.objects.get(pk=id)
        pi.delete()
        return redirect('stockdata')
    else:
        return redirect('stockdata')

def createInventory(request):
    form=InventoryForm()
    context={}
    invt=Inventory.objects.all()
    context['form']=form
    context['invt']=invt
    # print(request.POST['material'])
    if request.method == "POST" :
        form=InventoryForm(request.POST)
        # start=request.POST['starttime']
        # end=request.POST['endtime']
        
        # print('start',start)
        if form.is_valid():
            form.save()
            return redirect('createinventory')

    return render(request,'production/createInventory.html',context)

def inventorydata(request):
    context={}
    inventory=Inventory.objects.all()
    context['inventory']=inventory
    return render(request,'production/inventorydata.html',context)

def updateInventory(request,pk):  
    pack = Inventory.objects.get(id=pk)
    pack_form = InventoryForm(instance=pack)
    if request.method == 'POST':
        pack_form = InventoryForm(request.POST,instance=pack)
        pack_form.save()

        return redirect('createinventory')

    context = {'form':pack_form} 
    return render(request,'production/updateInventory.html',context)


def deleteInventory(request,pk):
    if request.user.is_admin:

        pi=Inventory.objects.get(pk=pk)
        pi.delete()
        # messages.success(request,"successful")
        return redirect('createinventory')
    else:
        # messages.success(request,"You don't have delete  permission")
        return redirect('createinventory')

def createSale(request):
    form=SaleForm()
    context={}
    context['form']=form
    
    if request.method == "POST" :
        form=SaleForm(request.POST)
        # start=request.POST['starttime']
        # end=request.POST['endtime']
        
        # print('start',start)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userdashboard')

    return render(request,'production/createSale.html',context)

def saledata(request):
    context={}
    sale=Sale.objects.all()
    context['sale']=sale
    return render(request,'production/saledata.html',context)

def saleinfo(request,id=None):
    context={}
    sale=Sale.objects.filter(pk=id).first()
    context['sale']=sale
    return render(request,'production/saleinfo.html',context)


def updateSale(request,pk):  
    pack = Sale.objects.get(id=pk)
    pack_form = SaleForm(instance=pack)
    if request.method == 'POST':
        pack_form = SaleForm(request.POST,instance=pack)
        pack_form.save()

        return redirect('userdashboard')

    context = {'form':pack_form} 
    return render(request,'production/createSale.html',context)
# Generate a PDF File Venue List
def sale_pdf(request,pk):
	# Create Bytestream buffer
    buf = io.BytesIO()
	# Create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
	# Create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)
	
	# Designate The Model
    sale = Sale.objects.get(id=pk)
	# Create blank list
    lines = []
    lines.append("Details")
    lines.append("-------------------------------------------")
    # lines.append("Invoice No   :{} ".format(str(invoice.Invoice_number)))
    # lines.append("Payment Term :{} ".format(str(invoice.payment_terms)))
    # lines.append("Service Name :{} ".format(str(invoice.service.name)))
    lines.append("Item :{} ".format(str(sale.item.available_item.name)))
    lines.append("Description  :{} ".format(str(sale.description)))
    lines.append("Date         :{} ".format(str(sale.Date)))
    lines.append("--------------------------------------------")
    lines.append("Quantity     :{} ".format(str(sale.Qty)))
    lines.append("Rate         :{} ".format(str(sale.rate)))
    lines.append("Discount     :{} ".format(str(sale.Discount)))
    lines.append("Tax          :{} ".format(str(sale.Tax)))
    lines.append("----------------------------------------------")
    lines.append("Total        :{} ".format(str(sale.Total)))
	# Loop
    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

	# Return something
    return FileResponse(buf,as_attachment=True,filename='sale.pdf')

def createEqcategory(request):
    form=EqCategoryForm()
    context={}
    context['form']=form
    material=EqCategory.objects.all()
    context['material']=material
    if request.method == "POST" :
        form=EqCategoryForm(request.POST)

        # start=request.POST['starttime']
        # end=request.POST['endtime']
        
        # print('start',start)
        if form.is_valid():
            form.save()
            context[material]=EqCategory.objects.all()
            return redirect('createEqcategory')

    return render(request,'production/categorydata.html',context)


# def materialinfo(request,pk):
#     material = Material.objects.get(id=pk)
#     return render(request,'production/materialinfo.html',{'material':material})


def updateEqcategory(request,pk): 
    context={} 
    material2 = EqCategory.objects.get(pk=pk)
    form = EqCategoryForm(instance=material2)
    material=EqCategory.objects.all()
    context['material']=material
    if request.method == 'POST':
        form = EqCategoryForm(request.POST,instance=material2)
        form.save()

        return redirect('createEqcategory')

    context ['form']=form
    return render(request,'production/categorydata.html',context)

def deleteEqcategory(request,id):
    if request.user.is_admin:

        pi=EqCategory.objects.get(pk=id)
        pi.delete()
        # messages.success(request,"successful")
        return redirect('createEqcategory')
    else:
        # messages.success(request,"You don't have delete  permission")
        return redirect('createEqcategory')


def createTransport(request):
    form=TransportForm()
    context={}
    context['form']=form
    if request.method == "POST" :
        form=TransportForm(request.POST)
        # start=request.POST['starttime']
        # end=request.POST['endtime']
        
        # print('start',start)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transportdata')

    return render(request,'production/createTransport.html',context)

def transportdata(request):
    context={}
    transport=Transport.objects.all()
    context['transport']=transport
    return render(request,'production/transportdata.html',context)

def transportinfo(request,id=None):
    context={}
    transport=Transport.objects.filter(pk=id).first()
    context['transport']=transport
    return render(request,'production/transportinfo.html',context)


def updatetransport(request,pk):  
    pack = Transport.objects.get(id=pk)
    form = TransportForm(instance=pack)
    if request.method == 'POST':
        form = TransportForm(request.POST,instance=pack)
        form.save()

        return redirect('transportdata')

    context = {'form':form} 
    return render(request,'production/createTransport.html',context)

def deletetransport(request,id):
    if request.user.is_admin:

        pi=Transport.objects.get(pk=id)
        pi.delete()
        return redirect('transportdata')
    else:
        return redirect('transportdata')

def createEQ(request):
    form=EQForm()
    context={}
    context['form']=form
    eq=Equipment.objects.all()
    context['eq']=eq
    if request.method == "POST" :
        form=EQForm(request.POST)

        # start=request.POST['starttime']
        # end=request.POST['endtime']
        
        # print('start',start)
        if form.is_valid():
            form.save()
            context[eq]=Equipment.objects.all()
            return redirect('createEQ')

    return render(request,'production/createEQ.html',context)


# def materialinfo(request,pk):
#     material = Material.objects.get(id=pk)
#     return render(request,'production/materialinfo.html',{'material':material})


def updateEQ(request,pk):  
    eq = Equipment.objects.get(pk=pk)
    form = EQForm(instance=eq)
    if request.method == 'POST':
        form = EQForm(request.POST,instance=eq)
        form.save()

        return redirect('createEQ')

    context = {'form':form} 
    return render(request,'production/createEQ.html',context)

def deleteEQ(request,id):
    if request.user.is_admin:

        pi=Equipment.objects.get(pk=id)
        pi.delete()
        # messages.success(request,"successful")
        return redirect('createEQ')
    else:
        # messages.success(request,"You don't have delete  permission")
        return redirect('createEQ')