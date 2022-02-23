from django.urls import path
from . import views

urlpatterns = [
    
    # path('packageinfo',views.ListUserSalaryPackageView.as_view(),name = 'details'),
    # path('packageinfo/add/',views.CreateUserSalaryPackageView.as_view(),name = 'add'),
    # path('packageinfo/<pk>/edit/',views.UpdateUserPaymentReceiptView.as_view(),name = 'put'),

    # path('package',api.ListEmployeePackageView.as_view(),name = 'details'),
    # path('package/add/',api.CreateEmployeePackageView.as_view(),name = 'add'),
    # path('package/<pk>/edit/',api.UpdateEmployeePackageView.as_view(),name = 'put'),

    # path('salary',api.ListUserMonthlySalaryView.as_view(),name = 'details'),
    # path('salary/add/',api.CreateUserMonthlySalaryView.as_view(),name = 'add'),
    # path('salary/<pk>/edit/',api.UpdateUserMonthlySalaryBillView.as_view(),name = 'put'),
    path('empack/',views.EmployeePackageListCreateView.as_view(),name = 'empack'),
    path('empack/<pk>/',views.EmployeePackageDetailView.as_view(),name = 'empack-del'),
    path('monthsal/',views.MonthlySalaryListCreateView.as_view(),name = 'monthsal'),
    path('monthsal/<pk>/',views.MonthlySalaryDetailView.as_view(),name = 'monthsal-del'),
    

]