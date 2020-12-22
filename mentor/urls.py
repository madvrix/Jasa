from django.contrib import admin
from django.urls import path
from mentor import views

urlpatterns = [
    path('', views.mhome, name='mhome'),
    path('detail/', views.mdetail, name='mdetail'),
]