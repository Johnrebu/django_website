"""
URL configuration for john project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from MyFirstApplication import views as v1
from secondApp import views as v2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', v1.homepage),
    path('',v1.home),
    path('login/',v1.login),
    path('register/',v1.register),
    path('payment/',v1.payment),
    path('second/',include("secondApp.urls")),
    path('model/',include("ModelApp.urls")),
    path('alert/',include("AlertApp.urls")),
    path('crud/',include("CRUDApp.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path('rest/',include('RestApp.urls'))
]
