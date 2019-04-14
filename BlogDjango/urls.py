"""BlogDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from blog.urls import app_name
from django.contrib import admin, auth
from django.urls import include, path
from blog.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/login', auth.views.LoginView.as_view(), name="login"),
    path('auth/logout', auth.views.LogoutView.as_view(),
         name="logout", kwargs={'next_page': '/'}),
    path('auth/register', register, name="registration"),
    path('', include('blog.urls'))
]
