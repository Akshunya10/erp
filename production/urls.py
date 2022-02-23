from django.urls import path
from . import views

urlpatterns=[
    path('c_productmaterial/',views.createProductmat,name='createproductmat'),
    path('productmaterialdata/',views.productmatdata,name='productmatdata'),
    path('u_productmaterial/<pk>/',views.updateproductmat,name='updateproductmat'),
    path('productmatinfo/<id>/',views.productmatinfo,name='productmatinfo'),
    path('d_productmaterial/<id>/',views.deleteproductmat,name='deleteproductmat'),

    path('c_material/',views.creatematerial,name='creatematerial'),
    path('updatematerial/<pk>',views.updatematerial,name='updatematerial'),
    path('deletematerial/<id>/',views.deletematerial,name='deletematerial'),

    path('c_inventory/',views.createInventory,name='createinventory'),
    path('inventorydata/',views.inventorydata,name='inventorydata'),
    path('u_inventory/<pk>/',views.updateInventory,name='updateinventory'),
    path('d_inventory/<pk>/',views.deleteInventory,name='deleteinventory'),

    path('createstock/',views.createstock,name='createstock'),
    path('stockdata/',views.stockdata,name='stockdata'),
    path('stockinfo/<id>',views.stockinfo,name='stockinfo'),
    path('u_stock/<pk>/',views.updatestock,name='updatestock'),
    path('d_stock/<id>/',views.deletestock,name='deletestock'),

    path('c_sale/',views.createSale,name='createSale'),
    path('saleinfo/<id>',views.saleinfo,name='saleinfo'),
    path('saledata/',views.saledata,name='saledata'),
    path('u_sale/<pk>/',views.updateSale,name='updateSale'),
    path('salepdf/<pk>/',views.sale_pdf,name='salepdf'),

    path('c_category/',views.createEqcategory,name='createEqcategory'),
    path('updatecategory/<pk>',views.updateEqcategory,name='updateEqcategory'),
    path('deletecategory/<id>/',views.deleteEqcategory,name='deleteEqcategory'),

    path('c_transport/',views.createTransport,name='createtransport'),
    path('transportdata/',views.transportdata,name='transportdata'),
    path('u_transport/<pk>/',views.updatetransport,name='updatetransport'),
    path('d_transport/<id>/',views.deletetransport,name='deletetransport'),
    path('transportinfo/<id>/',views.transportinfo,name='transportinfo'),

    path('createEQ/',views.createEQ,name='createEQ'),
    path('updateEQ/<pk>',views.updateEQ,name='updateEQ'),
    path('deleteEQ/<id>/',views.deleteEQ,name='deleteEQ'),


]
