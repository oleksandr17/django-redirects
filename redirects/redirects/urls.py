"""redirects URL Configuration

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
from django.contrib import admin
from django.urls import path

from .views import (RandomAnimalView, SearchRedirectView,
                    redirect_success_view, redirect_view)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('redirect/', redirect_view),
    path('redirect-success/', redirect_success_view, name='redirect-success'),
    path('search/<term>/', SearchRedirectView.as_view()),
    path('random-animal/', RandomAnimalView.as_view()),
]
