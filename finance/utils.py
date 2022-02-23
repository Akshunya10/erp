# Arithmatic Operations Logics (*,+,/,-)

from django.shortcuts import render,redirect
from .models import *
from services.models import *

def total(request,pk,*args,**kwargs):
    invoice = Invoice.objects.get(id = pk)
    qs = invoice.serviceentry_set.all()
    s = 0
    for q in qs.iterator():
        s += q.rate
    
    context = {'sum': s}
    return render(request,'finance/invinfo.html',context)