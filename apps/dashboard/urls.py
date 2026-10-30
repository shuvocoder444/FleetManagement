from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_router, name='index'),
    path('superadmin/', views.superadmin_dashboard, name='superadmin'),
    path('admin/', views.admin_dashboard, name='admin'),
    path('company/', views.admin_dashboard, name='company'),
    path('driver/', views.driver_dashboard, name='driver'),
]
