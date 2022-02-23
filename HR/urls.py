from django.urls import path
from . import views
from . import api

urlpatterns = [
    
    path('hr/',views.hr,name='hr'),
    path('',views.hrHome,name='hrHome'),

    path('dept/', views.dept, name = 'dept'),
    path('dept/<pk>/', views.deptinfo, name = 'deptinfo'),
    path('create_department/', views.createdept, name = 'createdept'),
    path('update_department/<pk>/',views.updatedept,name='update_dept'),
    path('delete_dept/<pk>/',views.deleteDept,name='delete_dept'),
   


    path('staff/', views.staff, name = 'staff'),
    path('staff/<pk>/', views.staffinfo, name = 'staffinfo'),
    path('create_staff/', views.createstaff, name = 'createstaff'),
    path('update_staff/<pk>/',views.updatestaff,name='update_staff'),
    path('delete_staff/<pk>/',views.deleteStaff,name='delete_staff'),

]

