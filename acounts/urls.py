# from django.contrib import admin
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.tampilkan),
    
# ]
from django.conf.urls import url
from django.urls import path
from . import views# SET THE NAMESPACE!
app_name = 'acounts'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
]