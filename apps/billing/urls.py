from django.urls import path
from . import views

app_name = 'billing'

urlpatterns = [
    path('manual-payments/', views.manual_payments_list, name='manual_payments'),
    path('manual-payments/<int:pk>/approve/', views.approve_payment, name='approve_payment'),
    path('manual-payments/<int:pk>/reject/', views.reject_payment, name='reject_payment'),
    path('subscriptions/', views.subscriptions_list, name='subscriptions'),
    path('plans/', views.plans_list, name='plans'),
]
