from django.contrib import admin
from .models import *
from services.models import *
from django.db.models import Sum,F

admin.site.register(Invoice)
admin.site.register(JournalEn)
admin.site.register(PaymentEn)
admin.site.register(ContraEn)
admin.site.register(ReceiptEn)
admin.site.register(PurchaseOrder)
admin.site.register(Ledger)


                                                   #----------------------------------FOR ADDING SERVICES

# class ServiceEntryInline(admin.TabularInline):
#     model = ServiceEntry
#     extra = 1

#     readonly_fields = ['unit_price','amount']              
    
#     def unit_price(self,obj):
#         return "$" + str((obj.rate))


#     def amount(self,obj):                                                                       
#         value = (obj.service.cost * obj.Qty) - (((obj.Discount)/100) * (obj.Qty * obj.service.cost))     # important: taking value from Service model
#         return "$" + str(float(value + obj.Tax))                                                          # i.e service.cost
#                                                                                                            # till now this is the only solution
#                                                                                                             # gives error on obj.rate instead of obj.service.cost
    
    


# class InvoiceAdmin(admin.ModelAdmin):
#     inlines = [ServiceEntryInline]                        # ,ServiceTotalInline
    
#     def save_model(self, request, obj, form, change):                            ######################### To save the child class before parent
#         if not obj.pk: # call super method if object has no primary key 
#             super(InvoiceAdmin, self).save_model(request, obj, form, change)
#         else:
#             pass # don't actually save the parent instance

#     def save_formset(self, request, form, formset, change):
#         formset.save() # this will save the children
#         form.instance.save()

#     class Meta:
#         model = Invoice
#         fieldsets = (
#         (None, {
#             'fields':('from_company',
#                      'customer_name',
#                      'Invoice_number',
#                      'cust_sno',
#                      'Invoice_date',
#                      )
#             }),
#     )
    # readonly_fields = ['customer_ID']  #,'total'
    
    # def customer_ID(self,obj):
    #     return  str(obj.customer_name) + str(obj.from_company) + str(obj.id)
         

    # def total(self,obj,*args,**kwargs):         
    #     invoice = Invoice.objects.get(id=obj.id)
    #     entries = invoice.serviceentry_set.all()
    #     s = 0
    #     for q in entries.iterator():
    #         s += (q.rate * q.Qty) - (((q.Discount)/100) * (q.Qty * q.rate)) + q.Tax


    #     return "$" + str(s) 

    
        


                                                  #----------------------------------FOR ADDING PRODUCTS
# class ProductEntryInline(admin.TabularInline):
#     model = ProductEntry
#     extra = 1
#     readonly_fields = ['unit_price','amount']
    
#     def unit_price(self, obj):
#         return "$" + str(float(obj.Product.cost))

#     def amount(self, obj):
#         value = (obj.Product.cost * obj.Qty) - (((obj.Discount)/100) * (obj.Qty * obj.Product.cost))
#         return "$" + str(float(value + obj.Tax))





# class POAdmin(admin.ModelAdmin):
#     inlines = [ProductEntryInline]           # ,ProductTotalInline
    
#     def save_model(self, request, obj, form, change):         ######################### To save the child class before parent
#         if not obj.pk: # call super method if object has no primary key 
#             super(POAdmin, self).save_model(request, obj, form, change)
#         else:
#             pass # don't actually save the parent instance

#     def save_formset(self, request, form, formset, change):
#         formset.save() # this will save the children
#         form.instance.save()


#     class Meta:
#         model = PurchaseOrder
#         fieldsets = (
#         (None, {
#             'fields':('from_company',
#                     'vendor_name',
#                     'PO_Number',
#                     'vendor_sn',
#                     'PO_Date',
#                      )
#             }),
#     )
#     readonly_fields = ['vendor_ID']      #,'total'
    
#     def vendor_ID(self,obj):
#         return  str(obj.vendor_name) + str(obj.from_company) + str(obj.id)

    # def total(self,obj):
    #     # q = Service.objects.aggregate(Sum('cost'))
    #     qs = ProductEntry.objects.all()
    #     # ps = Service.objects.all()
    #     s = 0
    #     for q in qs.iterator():
    #         s += (q.rate * q.Qty) - (((q.Discount)/100) * (q.Qty * q.rate)) + q.Tax
        

    #     return "$" + str(s) 


# admin.site.register(PurchaseOrder,POAdmin)


