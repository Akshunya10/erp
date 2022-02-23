from django.urls import path
from . import views


urlpatterns = [
   
  

    path('invoice/', views.InvoiceListView.as_view(), name='invoice'),
    path('invoice/<pk>/', views.InvoiceView.as_view(), name='invoice-del'),

    path('po/',views.PoListCreateView.as_view(),name = 'po'),
    path('po/<pk>/',views.PoDetailView.as_view(),name = 'po-del'),


]
