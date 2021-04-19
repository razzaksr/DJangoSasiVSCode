from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.initial),
    path('valid',views.auth),
    path('show',views.show),
    path('candidate',views.candidate),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.remove),
]