
from django.contrib import admin
from django.urls import include,path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    
    path('admin/', admin.site.urls),   
    path('auth/',include('authentication.urls')),
    path('projectmanagement/',include('ProjectManagement.urls')),
    #templates urls
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    # path('',views.home,name='home'),
    # path('profile/', include('authentication.urls')),  
    path('finance/',include('finance.urls')),
    #path('project/',include('ProjectManagement.urls')),
    path('hr/',include('HR.urls')),
    path('payroll/',include('payroll.urls')),
    #path('sla/',include('ServiceLevelAgreement.urls')),
    path('service/',include('services.urls')), 
    path('production/',include('production.urls')), 
   
    
    # apis urls 
    path('api/auth/',include('authentication.Newapi.urls')),
    path('api/auth2/',include('authentication.api.urls')),
    path('api/finance/',include('finance.api.urls')),
    path('api/hr/',include('HR.api.urls')),
    path('api/payroll/',include('payroll.api.urls')),  
    path('api/services/',include('services.api.urls')), 
    path('api/pm/',include('ProjectManagement.urls')),
    path('api/sla/',include('ServiceLevelAgreement.urls')),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

