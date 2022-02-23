from django.urls import path
from . import views
from . import api

urlpatterns = [
    
    path('',views.financeHome,name='financeHome'),

    path('dashboard/',views.finance,name='finance'),

    # path('invoice/', views.invoice, name = 'invoice'),
    path('invoice/', views.invoice, name = 'invoices'),#addede sa30
    path('invoice/<pk>/', views.invinfo, name = 'invinfo'),
    path('invoicepdfview/<pk>/',views.invoice_pdf,name='invoicepdf'),
    path('create_invoice/',views.createinvoice,name='create_invoice'),
    path('update_invoice/<pk>/',views.updateinvoice,name='update_invoice'),
    path('update_inent/<pk>/',views.updateSEnt,name='update_inentry'),
    path('delete_invoice/<pk>/',views.deleteinvoice,name='delete_invoice'),
    path('delete_inent/<pk>/',views.deleteSEnt,name='delete_inentry'),
    path('invoiceApi/',views.InvoiceApiView.as_view()),
    path('invoiceApi/<int:pk>',views.UD_InvoiceApiView.as_view()),
    path('poApi/',views.PoApiView.as_view()),
    path('poApi/<int:pk>',views.UD_PoApiView.as_view()),


    # po - purchase order
    # path('po/', views.po, name = 'po'),
    path('po/', views.po, name = 'poS'),
    path('po/<pk>/', views.poinfo, name = 'poinfo'),
    path('create_po/',views.createPO,name='create_po'),
    path('update_po/<pk>/',views.updatePO,name='update_po'),
    path('popdfview/<pk>/',views.po_pdf,name='popdf'),

    path('update_poent/<pk>/',views.updatePEnt,name='update_poentry'),
    path('delete_po/<pk>/',views.deletePO,name='delete_po'),
    path('delete_poent/<pk>/',views.deletePEnt,name='delete_poentry'),

    path('receipts/',views.receipts, name='receipts_page'),
    path('journal/',views.journal, name='journal_page'),
    path('payment/',views.payments, name='payment_page'),
    path('contra/',views.contra, name='contra_page'),
    path('ledger/',views.ledgercreation, name='ledger_page'),
    path('balance/',views.balance_sheet, name='balance_page'),
    path('ledger_delete/<pk>/',views.ledger_delete, name='ledger_delete_page'),
    path('updateledger/<pk>/',views.updateledger, name='updateledger_page'),   
    path('updatejournal/<pk>/',views.updatejournal, name='updatejournal_page'),   
    path('updatereceipt/<pk>/',views.updatereceipt, name='updatereceipt_page'),   
    path('updatepayment/<pk>/',views.updatepayment, name='updatepayment_page'),   
    path('updatecontra/<pk>/',views.updatecontra, name='updatecontra_page'),   
    path('journal_delete/<pk>/',views.journaldelete, name='journal_delete_page'),
    path('receipt_delete/<pk>/',views.receiptdelete, name='receipt_delete_page'),
    path('payment_delete/<pk>/',views.paymentdelete, name='payment_delete_page'),
    path('contra_delete/<pk>/',views.contradelete, name='contra_delete_page'),
    path('pl/',views.profit_loss,name='profit-loss_page'),

]

# Journal
# Journal
# Receipts
# Payments 
# Contra
# Creating of ledgers/Accounts(Revenue, Cost,Expenses, Capital, Banks Liability,Fixed Asset etc)
# Profit and Loss accounts
# Balance Sheet
# Depreciation