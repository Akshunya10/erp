from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Material)
# class ProductionMaterialModeladmin(admin.ModelAdmin):
#     def formfield_for_manytomany(self, db_field, request, **kwargs):
#         if db_field.name == 'material':
#             kwargs["queryset"] = Productwithqty.objects.filter(active=True)
#         return super().formfield_for_manytomany(db_field, request, **kwargs)

admin.site.register(ProductionMaterial)
admin.site.register(Inventory)
admin.site.register(Sale)
admin.site.register(EqCategory)

admin.site.register(Equipment)

admin.site.register(Transport)
admin.site.register(Productwithqty)
admin.site.register(Stock)