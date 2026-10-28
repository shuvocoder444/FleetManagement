from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('users/', views.users_list, name='users'),
]
