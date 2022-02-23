from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token
from . import views
# app_name = 'authentication'

urlpatterns = [
    #custom auth api
    # path('',views.AuthAPI.as_view()),  
    # JWT
    #path('jwt/',obtain_jwt_token),
   # path('jwt/refresh/',refresh_jwt_token),
    
    #path('register/',views.RegistrationAPIView.as_view(),name = 'register'),
    #path('login/',views.LoginAPIView.as_view()),

    #path('user/',views.UserListCreateView.as_view(),name = 'user'),
    #path('user/<pk>/',views.UserDetailView.as_view(),name = 'user-del'),

    path('com/',views.CompanyListCreateView.as_view(),name = 'company'),
    path('com/<pk>/',views.CompanyDetailView.as_view(),name = 'company-del'),

    path('emp/',views.EmployeeListCreateView.as_view(),name = 'employee'),
    path('emp/<pk>/',views.EmployeeDetailView.as_view(),name = 'employee-del'),

    path('cus/',views.CustomerListCreateView.as_view(),name = 'customer'),
    path('cus/<pk>/',views.CustomerDetailView.as_view(),name = 'customer-del'),

    path('ven/',views.VendorListCreateView.as_view(),name = 'vendor'),
    path('ven/<pk>/',views.VendorDetailView.as_view(),name = 'vendor-del'),
]


# from .views import CustomerViewSet
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'', CustomerViewSet, basename='user')
# urlpatterns = router.urls
# 88
