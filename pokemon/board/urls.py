from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('roll', views.roll),
    path('test', views.test),
]
