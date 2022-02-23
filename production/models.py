from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.db.models.signals import pre_save,post_save
from authentication.models import User
# Create your models here.

class Material(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(max_length=300)
    def __str__(self):
        return str(self.name)



class Productwithqty(models.Model):
    item=models.ForeignKey(Material,on_delete=models.CASCADE)
    quantity=models.FloatField()
    active=models.BooleanField(default=True)

    def __str__(self):
        return (self.item.name)+"--"+str(self.quantity)

class ProductionMaterial(models.Model):
    product_name=models.CharField(max_length=100)
    material=models.ManyToManyField(Productwithqty)
    produced_quantity=models.CharField(max_length=50)
    created_date=models.DateField(auto_now=True)

    # production_date=models.DateField(auto_now=True)
    # mix_duration=models.TimeField()
    def __str__(self):
        return self.product_name
# class CopyforProMat(models.Model):
#     ProductionMaterial=models.ForeignKey(ProductionMaterial, on_delete=models.CASCADE)
    


class Stock(models.Model):
    item=models.OneToOneField(ProductionMaterial, on_delete=models.CASCADE)
    quantity=models.CharField(max_length=50)
    created_date=models.DateField( auto_now=True)
    update_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.item.product_name)

class Inventory(models.Model):
    
    available_item=models.OneToOneField(Material, on_delete=models.CASCADE)
    quantity=models.CharField(max_length=50)

    def __str__(self):
        return str(self.available_item.name)

class Sale(models.Model):
    item                   = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    description            = models.TextField(max_length=250, blank=True, null=True)
    Date                = models.DateField()
    rate                   = models.FloatField(blank=True, null=True)    
    Qty                    = models.FloatField(blank=True, null=True)
    Discount               = models.FloatField(blank=True, null=True)
    Tax                    = models.FloatField(blank=True, null=True)
    Total                  = models.FloatField(blank=True, null=True,default=0)


def post_save_Saletotal(instance,sender,*args,**kwargs):

    inst_rate=instance.rate
    inst_Qty=instance.Qty
    inst_Discount=instance.Discount
    inst_Tax=instance.Tax
    saDis=inst_rate*inst_Qty*(inst_Discount/100)
    inst_Total = 0
    priceafterdis=((inst_rate*inst_Qty)-saDis)
    print('priceafterdis',priceafterdis)
    saTax=priceafterdis*(inst_Tax/100)
    print(saTax)
    instance.Total=priceafterdis+saTax
    print(inst_Total)
    q=inst_Total
    print(q)

# pre_save.connect(post_save_Saletotal, sender=Sale)

def update_inventory_on_sale(instance,sender,*args, **kwargs):
    item=instance.item
    qty=instance.Qty
    inv=Inventory.objects.filter(available_item__name=item).first()
    inv.quantity=float(inv.quantity)-float(qty)
    inv.save()

pre_save.connect(update_inventory_on_sale, sender=Sale)



# def po_no_generator(instance,sender,*args, **kwargs):
#     if not instance.PO_Number:
#         word="PO"
#         instance.PO_Number= word+"_"+str(instance.Vendor.company_name)+"_"+str(random_string_generator())

# pre_save.connect(po_no_generator,sender=PurchaseOrder)

class EqCategory(models.Model):
    category=models.CharField(max_length=100)
    def __str__(self):
        return self.category

class Equipment(models.Model):
    Id_no=models.CharField(max_length=100)
    category=models.ForeignKey(EqCategory,on_delete=models.CASCADE)
    description=models.TextField(max_length=300)
    registration_date=models.DateField()

class Transport(models.Model):
    equipment=models.OneToOneField(Equipment, on_delete=models.CASCADE)
    last_maintained=models.DateField()
    next_maintenance=models.DateField()
    responsible_person=models.ForeignKey(User, on_delete=models.CASCADE)
    remark=models.TextField()


    
   
def prodmat_inven_update(instance,sender,*args, **kwargs):
    qty=instance.produced_quantity
    pname=instance.product_name
    prodmat=ProductionMaterial.objects.filter(product_name=pname).first()

    try:
        obj = Stock.objects.get(item__product_name=pname)
        print('existing stock',float(obj.quantity))
        obj.quantity = float(obj.quantity)+float(qty)
        print('qt',qty)
        print('new obj.qt',obj.quantity)

        # print('existing stock',float(obj.quantity)+float(qty))
        obj.save()
    except Stock.DoesNotExist:
        # obj = Stock.objects.create(field=new_value)
        print(qty)
        b=Stock.objects.create(item=prodmat,quantity=qty)
        # print('existing stock')
        # print('existing stock',float(obj.quantity)+float(qty))
        b.save()

    # if exstock:
    #     s=exstock.update(quantity=exstock.quantity+qty)
    #     s=Stock.objects.filter(item__product_name=pname).update(quantity=exstock.quantity+qty)

    #     s.save()
    # else:
    #     b=Stock.objects.create(item=prodmat,quantity=qty)
    #     b.save()



#post_save.connect(prodmat_inven_update, sender=ProductionMaterial)
