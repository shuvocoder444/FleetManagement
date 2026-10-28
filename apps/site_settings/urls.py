from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('switch-currency/<str:code>/', views.switch_currency, name='switch_currency'),
    path('switch-language/<str:lang_code>/', views.switch_language, name='switch_language'),
]

