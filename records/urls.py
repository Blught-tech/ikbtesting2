from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_task, name='create_task'),
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
    path('profile/', views.user_profile, name='user_profile'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('', views.task_list, name='task_list'),
]
