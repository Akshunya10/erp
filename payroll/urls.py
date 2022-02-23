from django.urls import path
from . import views
from . import api
urlpatterns = [

    
    path('',views.payroll,name='payroll'),
    path('pay/',views.payrollHome,name='payrollHome'),

    path('empsal/', views.empsalary, name = 'empsal'),
    path('empsal/<pk>/', views.empsalinfo, name = 'empsalinfo'),
    path('create_empsal/',views.createEmpPac,name='create_empsal'),
    path('update_empsal/<pk>',views.updatePack,name='update_empsal'),
    path('delete_empsal/<pk>/',views.deletePack,name='delete_empsal'),

    path('monthsal/', views.monthsal, name = 'monthsala'),
    path('monthsal/<pk>/', views.monthsalinfo, name = 'monthsalinfo'),
    path('create_monthsal/',views.createMonthSal,name='create_sal'),
    path('create_monthsal/',views.createMonthSal,name='create_salv'),
    path('update_monthsal/<pk>',views.updateMonthSal,name='update_monthsal'),
    path('monthsalpdf/<pk>/',views.monthsal_pdf,name='monthsalpdf'),

    path('update_monthsal/<pk>',views.updateMonthSal,name='update_monthsalv'),
    path('delete_monthsal/<pk>/',views.deleteMonthSal,name='delete_monthsal'),
    path('delete_monthsal/<pk>/',views.deleteMonthSal,name='delete_monthsalv'),
    path('createovertime/',views.createovertime,name="createovertime"),
    path('employeeApi/',views.EmployeepackageApiView.as_view()),
    path('employeeApi/<int:pk>',views.UD_EmployeepackageApiView.as_view()),
    path('packageApi/',views.MonthlysalaryApiView.as_view()),
    path('packageApi/<int:pk>',views.UD_MonthlysalaryApiView.as_view()),

]


