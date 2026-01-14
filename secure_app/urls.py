"""
URL configuration for secure_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views # Import auth views
from records import views as records_views
from django.conf import settings
from django.contrib.staticfiles.views import serve as staticfiles_serve
from django.urls import re_path 

urlpatterns = [
    path('', records_views.home, name='home'),
    path('admin/logout/', auth_views.LogoutView.as_view(next_page='admin:login'), name='admin_logout'),
    path('admin/', admin.site.urls),
    path('records/', include('records.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # These lines provide login/logout routes
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', records_views.register, name='register'),
]

if not settings.DEBUG:
    urlpatterns += [
         re_path(r'^static/(?P<path>.*)$', staticfiles_serve, {'insecure': True}),
    ]
