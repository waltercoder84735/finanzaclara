from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('servicios/', views.servicios, name='servicios'),
    path('blog/', views.blog, name='blog'),
    path('tutoriales/', views.tutoriales, name='tutoriales'),
    path('plantillas/', views.plantillas, name='plantillas'),
    path('contacto/', views.contacto, name='contacto'),
    path('buscar-cliente/', views.buscar_cliente, name='buscar_cliente'),
    path('about/', views.about, name='about'),
]
