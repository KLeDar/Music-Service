"""MusicService URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.contrib.auth import views
from music.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', GuestView.as_view(), name='guest'),
    path('main/', MainView.as_view(), name='main'),
    path('add_to_favorites/', add_to_favorites, name='add_to_favorites'),
    # Процессы аутентификации
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]

handler404 = custom_handler404
handler500 = custom_handler500