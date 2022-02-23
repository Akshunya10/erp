from django.urls import path
from . import views

urlpatterns = [
    
    path('service/',views.ServiceListCreateView.as_view(),name = 'service-info'),
    path('service/<pk>/',views.ServiceDetailView.as_view(),name = 'service-del'),
    path('plan/',views.PlanListCreateView.as_view(),name = 'plan'),
    path('plan/<pk>/',views.PlanDetailView.as_view(),name = 'plan-del'),
    path('product/',views.ProductListCreateView.as_view(),name = 'product'),
    path('product/<pk>/',views.ProductDetailView.as_view(),name = 'product-del'),
]

