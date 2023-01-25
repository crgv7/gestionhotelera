from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', views.ofertas),
    path('add/<id>/', views.add_oferta),
    path('panel/', views.panel),
    path("editar/<id>", views.editar),
    path("eliminar/<id>", views.eliminar),
   
    
]