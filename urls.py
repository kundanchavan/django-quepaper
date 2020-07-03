from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('form/', views.contact, name="contact"),
    path('form20/', views.formmark20, name="form20"),
    ]
