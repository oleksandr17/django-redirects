from django.contrib import admin
from django.urls import path

from .views import (RandomAnimalView, SearchRedirectView,
                    redirect_success_view, redirect_view)

urlpatterns = [
    path('redirect/', redirect_view),
    path('redirect-success/', redirect_success_view, name='redirect-success'),
    path('search/<term>/', SearchRedirectView.as_view()),
    path('random-animal/', RandomAnimalView.as_view()),
]
