"""turismagency URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from siteapp import views
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_hello),
    path('register/', views.register, name='register'),
    path('login/', views.submit_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register_travel/', views.register_travel, name='register_travel'),
    path('register_travel_insurance/', views.register_travel_insurance, name='register_travel_insurance'),
    path('view_info_travels/', views.view_info_travels, name='view_info_travels'),
    path('register_comment/', views.register_comment, name='register_comment'),
    
]
    

urlpatterns += staticfiles_urlpatterns()
