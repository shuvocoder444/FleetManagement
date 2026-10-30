from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_router, name='index'),
    path('superadmin/', views.superadmin_dashboard, name='superadmin'),
    path('admin/', views.admin_dashboard, name='admin'),
    path('company/', views.admin_dashboard, name='company'),
    path('driver/', views.driver_dashboard, name='driver'),
    path('driver/vehicle/', views.driver_vehicle_view, name='driver_vehicle'),
    path('driver/agreements/', views.driver_agreements_view, name='driver_agreements'),
    path('driver/history/', views.driver_history_view, name='driver_history'),
]
