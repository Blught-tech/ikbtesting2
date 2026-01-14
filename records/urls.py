from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.user_profile, name='user_profile'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/add/', views.create_task, name='create_task'),
    path('tasks/toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
    path('', views.home, name='home'),
]
