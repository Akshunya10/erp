from django.urls import path
from .import views

urlpatterns = [
         path('SLA/', views.SLAList.as_view(), name='details'),
         path('',views.SLHome,name='serviceagreementHome'),
        # path('add/', views.SLACreateAPIView.as_view(), name='add'),
         path('SLA/<pk>/', views.SLADetailView.as_view(), name='put'),
         path('History/', views.HistoryList.as_view(), name='details'),
        # path('Escalation', views.EscalationCreateAPIView.as_view(), name='add'),
        # path('Escalation/<ticket_no>/edit/', views.EscalationUpdateAPIView.as_view(), name='put'),
        # path('',views.sla,name='sla')
]
