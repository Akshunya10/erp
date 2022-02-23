from django.db.models import fields
from django.db.models.fields import DateField
from django.forms import ModelForm, widgets
from .models import *
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'
	
class TimeInput(forms.TimeInput):
	input_type="time"

class ProductmatForm(ModelForm):

    class Meta:
        model=ProductionMaterial
        fields='__all__'
        exclude=['material','produced_quantity','created_date']
        widgets = {
            
            'mix_duration': TimeInput(),
            
        }
    # def get_form(self, *args, **kwargs):
    #     form = super().get_form(*args, **kwargs)  # Get the form as usual
    #     # user = self.request.user
    #     form.fileds['material'].queryset = Productwithqty.objects.filter(active=True)
    #     return form

    

class MaterialForm(ModelForm):
    class Meta:
        model=Material
        fields='__all__'

class InventoryForm(ModelForm):
    class Meta:
        model=Inventory
        fields='__all__'

class SaleForm(ModelForm):
    class Meta:
        model=Sale
        fields='__all__'
        widgets={
            'Date':DateInput()
        }
        exclude=['Total']

class TransportForm(ModelForm):
    class Meta:
        model=Transport
        fields='__all__'
        widgets={
            'last_maintained':DateInput(),
            'next_maintenance':DateInput(),
        }

class EqCategoryForm(ModelForm):
    class Meta:
        model=EqCategory
        fields='__all__'

class ProdwithQtyForm(ModelForm):
    class Meta:
        model=Productwithqty
        fields='__all__'
        exclude=['active']

class StockForm(ModelForm):
    class Meta:
        model=Stock
        fields='__all__'


class EQForm(ModelForm):
    class Meta:
        model=Equipment
        fields='__all__'
        widgets={
            'registration_date':DateInput(),
        }