# from django.shortcuts import render,redirect
# from .models import Invoice,PurchaseOrder
# from .serializer import InvoiceSerializer,PurchaseOrderSerializer
# from rest_framework.authentication import SessionAuthentication
# from rest_framework import generics,mixins
# from services.models import *
# from .forms import *

#                                         # Invoice view
# class CreateInvoiceView(mixins.ListModelMixin,
#                         mixins.DestroyModelMixin,
#                         generics.CreateAPIView):
#     queryset                = Invoice.objects.all()
#     serializer_class        = InvoiceSerializer
#     permission_classes      =   []
#     authentication_classes  =   [SessionAuthentication]
#     lookup_field = 'pk'

#     def get(self,request,*args,**kwargs):
#         return  self.list(request,*args,**kwargs)

#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

#     def perform_create(self,serializer):
#         user    = self.request.user
#         serializer.save(user=user)


# # class ListInvoiceView(generics.ListAPIView):
# #     queryset = Invoice.objects.all()
# #     serializer_class = InvoiceSerializer
# #     permission_classes      =   []
# #     authentication_classes  =   []

# # class UpdateInvoiceView(generics.UpdateAPIView):
# #     queryset = Invoice.objects.all()
# #     serializer_class = InvoiceSerializer
# #     permission_classes      =   []
# #     authentication_classes  =   []
# #     lookup_field = 'customer_name'

                                         
# #                                          # PurchaseOrder view
# # class CreatePurchaseView(generics.CreateAPIView):
# #     queryset = PurchaseOrder.objects.all()
# #     serializer_class = PurchaseOrderSerializer
# #     permission_classes      =   []
# #     authentication_classes  =   []

# # class ListPurchaseView(generics.ListAPIView):
# #     queryset = PurchaseOrder.objects.all()
# #     serializer_class = PurchaseOrderSerializer
# #     permission_classes      =   []
# #     authentication_classes  =   []

# # class UpdatePurchaseView(generics.UpdateAPIView):
# #     queryset = PurchaseOrder.objects.all()
# #     serializer_class = PurchaseOrderSerializer
# #     permission_classes      =   []
# #     authentication_classes  =   []
# #     lookup_field = 'vendor_name'