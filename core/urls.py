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
    path('blog/<int:pk>/', views.detalle_articulo, name='detalle_articulo'),
    path('blog/crear/', views.crear_articulo, name='crear_articulo'),    
    path('blog/<int:pk>/editar/', views.editar_articulo, name='editar_articulo'),
    path('blog/<int:pk>/eliminar/', views.eliminar_articulo, name='eliminar_articulo'),
    ]
