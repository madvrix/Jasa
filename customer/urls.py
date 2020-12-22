from django.contrib import admin
from django.urls import path
from . import views
from customer.views import Cari

urlpatterns = [
    path('', views.chome, name='chome'),
    path('profil/', views.profil, name='profilcustomer'),
    path('<id>/profilgr', views.profilgr, name='profil'),
    path('<no>/form', views.form),
    path('<no>/formklien', views.formklien),
    path('paketform/',views.addpaket, name='paket_url'),
    path('<no_pkt>/hari',views.addhari),
    path('<no_pkt>/delpaket', views.delpaket, name='pktdel'),
    path('guru/', views.guru, name='guru'),
    path('search2', Cari.as_view(), name='search2')
]