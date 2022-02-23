from django.urls import path
from . import views
from .api import *
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    
    
    path('',views.profile,name = 'profile'),

    # sa30 Api
    path('registerApi/',views.RegisterApiView.as_view()),
    path('registerApi/<int:pk>',views.UD_RegisterApiView.as_view()),
    path('loginApi/',views.LoginWithTokenAuthenticationAPIView.as_view()),
    path('positionApi/',views.PositionApiView.as_view()),
    path('positionApi/<int:pk>',views.UD_PositionApiView.as_view()),
    path('departmentApi/',views.DepartmentApiView.as_view()),
    path('departmentApi/<int:pk>',views.UD_DepartmentApiView.as_view()),
    path('businessApi/',views.BusinessApiView.as_view()),
    path('businessApi/<int:pk>',views.UD_BusinessApiView.as_view()),
    path('customerApi/',views.CustomerApiView.as_view()),
    path('customerApi/<int:pk>',views.UD_CustomerApiView.as_view()),
    #sa30 
    path('addcustomernew/',views.customernew_view,name="addcustomernew"),
    path('updatecustomernew/<int:id>',views.customernewupdate,name="customernewupdate"),
    path('deletecustomernew/<int:id>',views.customernewdelete_view,name="customernewdelete"),
    path('addvendornew/',views.vendornew_view,name="addvendornew"),
    path('updatevendornew/<int:id>',views.vendornewupdate,name="vendornewupdate"),
    path('deletevendornew/<int:id>',views.vendornewdelete_view,name="vendornewdelete"),

    path('register/',views.registraiton_view,name="register"),
    path('userupdate1/<int:id>',views.userupdate1,name="userupdate"),
    path('position/',views.position_view,name="position"),
    path('positiondelete/<int:id>',views.positiondelete_view,name="positiondelete"),
    path('positionupdate/<int:id>',views.positionupdate,name="positionupdate"),
    path('department/',views.department_view,name="department"),
    path('departmentdelete/<int:id>',views.departmentdelete_view,name="departmentdelete"),
    path('departmentupdate/<int:id>',views.departmentupdate,name="departmentupdate"),
    path('business/',views.business_view,name="business"),
    path('businessdelete/<int:id>',views.businessdelete_view,name="businessdelete"),
    path('businessupdate/<int:id>',views.businessupdate,name="businessupdate"),
    path('login/',views.userLogin_view,name="userlogin"),
    path('logout/',views.userLogout_view,name="userlogout"),
    path('dashboard/',views.userdashboard_view,name="userdashboard"),
    path('addcompany/',views.addcompany,name="addcompany"),
    path('company/<int:pk>',views.compinfo,name="companyinfo"),
    path('companyupdate/<int:id>',views.compupdate,name="companyupdate"),
    path('companydelete/<int:id>',views.compdelete,name="companydelete"),
    path('contactperson/<int:id>',views.contactperson_view,name="contactperson"),
    path('addcontactperson/',views.addcontactperson,name="addcontactperson"),
    path('contactpersonupdate/<int:id>',views.contactpersonupdate,name="contactpersonupdate"),
    path('contactpersondelete/<int:id>',views.contactpersondelete,name="contactpersondelete"),
    path('contactpersonApi/',views.ContactpersonApiView.as_view()),
    path('contactpersonApi/<int:pk>',views.UD_ContactpersonApiView.as_view()),
    path('calenderview/',views.calenderview,name="calenderview"),
    path('userScorecard/',views.userScorecard,name="userScorecard"),

    


    
    # authentication/
    path('user/', views.indexview.as_view(), name = 'user'),

    path('customer/', views.customer, name = 'customers'),
    path('customer/<pk>/', views.customerinfo, name = 'customerinfo'),
    path('customerdelete/<id>/', views.customerdelete_view, name = 'customerdelete'),
    path('customerdetail/<id>/', views.customerdetail, name = 'customerdetail'),


    path('company/', views.company, name = 'company'),
    path('company/<pk>/', views.compinfo, name = 'compinfo'),
    path('companyApi/',views.CompanyApiView.as_view()),
    path('companyApi/<int:pk>',views.UD_CompanyApiView.as_view()),

    path('employee/', views.employee, name = 'employee'),
    path('employee/<pk>', views.empinfo, name = 'empinfo'),

    path('vendor/', views.vendor, name = 'vendor'),
    path('vendor/<pk>', views.vendinfo, name = 'vendinfo'),


    
    # path('register/', views.register, name='sign-up'),
    # path('login/', views.login, name='sign-in'),


]
    
    
 


