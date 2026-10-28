from django.urls import path
from . import views

app_name = 'drivers'

urlpatterns = [
    path('', views.driver_list, name='list'),
    path('create/', views.driver_create, name='create'),
    path('check/', views.check_driver_view, name='check'),
    path('<int:pk>/', views.driver_detail, name='detail'),
]
