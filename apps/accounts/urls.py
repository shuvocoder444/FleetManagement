from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('users/', views.users_list, name='users'),
    path('team/', views.team_members_view, name='team'),
    path('team/<int:pk>/delete/', views.team_member_delete, name='team_delete'),
    path('activity-log/', views.activity_log_view, name='activity_log'),
]
