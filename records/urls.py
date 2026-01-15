from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_task, name='create_task'),
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
    path('profile/', views.user_profile, name='user_profile'),
    path('mfa/setup/', views.mfa_setup, name='mfa_setup'),
    path('mfa/verify/', views.mfa_verify, name='mfa_verify'),
    path('mfa/disable/', views.mfa_disable, name='mfa_disable'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('', views.task_list, name='task_list'),
]
