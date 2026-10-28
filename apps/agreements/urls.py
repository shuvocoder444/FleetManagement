from django.urls import path
from . import views

app_name = 'agreements'

urlpatterns = [
    path('', views.agreement_list, name='list'),
    path('create/', views.agreement_create, name='create'),
]
