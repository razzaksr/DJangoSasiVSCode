from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.initial),
    path('valid',views.auth),
    path('feed',views.getEnroll),
    path('insert',views.setEnroll)
]