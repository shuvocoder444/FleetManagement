from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('about/', views.about_page, name='about'),
    path('features/', views.features_page, name='features'),
    path('pricing/', views.pricing_page, name='pricing'),
    path('contact/', views.contact_page, name='contact'),
    path('terms/', views.terms_page, name='terms'),
    path('privacy/', views.privacy_page, name='privacy'),
    path('settings/', views.settings_view, name='settings'),
    path('settings/pages/', views.pages_list_view, name='pages_list'),
    path('settings/pages/<slug:slug>/edit/', views.page_edit_view, name='page_edit'),
    path('switch-currency/<str:code>/', views.switch_currency, name='switch_currency'),
    path('switch-language/<str:lang_code>/', views.switch_language, name='switch_language'),
]


