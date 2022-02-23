from django.urls import path
from . import views

urlpatterns = [
    
    # path('department',api.ListDepartmentView.as_view(),name = 'details'),
    # path('department/add/',api.CreateDepartmentView.as_view(),name = 'add'),
    # path('department/<deptId>/edit/',api.UpdateDepartmentView.as_view(),name = 'put'),

    # path('profile',views.ListStaffProfileView.as_view(),name = 'details'),
    # path('profile/add/',views.CreateStaffProfileView.as_view(),name = 'add'),
    # path('profile/<pk>/edit/',views.UpdateStaffProfileView.as_view(),name = 'put'),

    # path('role',api.ListStaffProfileView.as_view(),name = 'details'),
    # path('role/add/',api.CreateStaffProfileView.as_view(),name = 'add'),
    # path('role/<pk>/edit/',api.UpdateStaffProfileView.as_view(),name = 'put'),
    path('dept/',views.DepartmentListCreateView.as_view(),name = 'dept'),
    path('dept/<pk>/',views.DepartmentDetailView.as_view(),name = 'dept-del'),
    path('staff/',views.StaffProfileListCreateView.as_view(),name = 'staff'),
    path('staff/<pk>/',views.StaffProfileDetailView.as_view(),name = 'staff-del'),
    

]