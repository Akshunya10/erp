# from django.contrib import admin
# from .models import EmployeeAccount,CustomerAccount,User
# # from django.contrib.auth.models import Group

# admin.site.register(User)
# admin.site.register(EmployeeAccount)
# admin.site.register(CustomerAccount)

from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# from django.contrib.admin import AdminSite

# from .forms import CustomUserChangeForm #CustomUserCreationForm,
from .models import User


admin.site.unregister(Group)
admin.site.register(EmployeeProfile)
admin.site.register(Position)

admin.site.register(Company)
admin.site.register(ContactPerson)
admin.site.register(Department)
admin.site.register(Business)
admin.site.register(CustomerNew)
admin.site.register(VendorNew)
# class CustomUserAdmin(UserAdmin):
#     model = User
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm

admin.site.register(User) # ,CustomUserAdmin


# from django.db import models
# from django.forms import CheckboxSelectMultiple

# class MyModelAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.ManyToManyField: {'widget': CheckboxSelectMultiple},
#     }

# class CustomerAdmin(admin.ModelAdmin):
                
#     class Meta:
#         model = Customer
        
#     # readonly_fields = ['customer_ID']
    
#     # def customer_ID(self,obj):
#     #     return  str(obj.first_name) + str(obj.id)



class VendorAdmin(admin.ModelAdmin):
                
    class Meta:
        model = Vendor
        
    readonly_fields = ['vendor_ID']
    
    def vendor_ID(self,obj):
        return  str(obj.first_name) + str(obj.id)



admin.site.register(Customer)#,CustomerAdmin)
admin.site.register(Vendor,VendorAdmin)
