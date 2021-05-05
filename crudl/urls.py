from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.initial),
    path('valid',views.auth),
    path('parent',views.parent),
    path('show',views.show),
    path('comshow',views.comshow),
    path('candidate',views.candidate),
    path('company',views.company),
    path('edit/<int:id>',views.edit),
    path('editcom/<int:id>',views.editcom),
    path('update/<int:id>',views.update),
    path('updatecom/<int:id>',views.updatecom),
    path('delete/<int:id>',views.remove),
    path('deletecom/<int:id>',views.removecom),
    path('find',views.find),
    path('findcom',views.findcom),
    path('look',views.look),
    path('lookcom',views.lookcom),
    path('hard',views.printing)
]