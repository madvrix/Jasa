from django.contrib import admin
from django.urls import path
from . import views
from dashboard.views import SearchView

urlpatterns = [
    path('', views.home, name='home'),
    path('<id>/profildashboard', views.profildashboard, name='profildashboard'),
    path('guru/', views.guruf, name='guruf'),
    path('search', SearchView.as_view(), name='search')
]