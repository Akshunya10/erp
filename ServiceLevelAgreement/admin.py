from django.contrib import admin

from .models import *


class SLAAdmin(admin.ModelAdmin):
    class Meta():
        model     =        SLA
    readonly_fields      =      ['Ticket_no']

    def Ticket_no(self,obj):
        return (obj.id)

admin.site.register(SLA,SLAAdmin)




admin.site.register(History)
#admin.site.register(Record)










