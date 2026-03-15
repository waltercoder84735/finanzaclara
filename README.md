# Finanzas Claras

Web de consultoría financiera para Pymes y personas, desarrollada con Django.

## Descripción
Finanzas Claras es una plataforma web que ofrece servicios de asesoramiento 
financiero para Pymes y personas con poca experiencia en finanzas personales. 
Incluye un blog, tutoriales en video, plantillas gratuitas descargables y 
formulario de contacto.

## Requisitos
- Python 3.x
- Django 6.x

## Instalación
1. Clonar el repositorio
2. Instalar Django: pip install django
3. Ejecutar migraciones: python manage.py migrate
4. Crear superusuario: python manage.py createsuperuser
5. Iniciar servidor: python manage.py runserver

## Orden para probar las funcionalidades
1. Ir a /servicios para ver los servicios disponibles
2. Ir a /blog para ver los artículos publicados
3. Ir a /tutoriales para ver los tutoriales disponibles
4. Ir a /plantillas para ver y descargar las plantillas gratuitas
5. Ir a /contacto para registrar un mensaje
6. Ir a /buscar-cliente para buscar clientes registrados
7. Ir a / para usar el buscador general desde el inicio
8. Ir a /admin para acceder al panel de administración

## Modelos
- Servicio: servicios ofrecidos por Finanzas Claras
- Articulo: publicaciones del blog
- Cliente: personas que contactan para contratar servicios
- Tutorial: videos cortos sobre finanzas
- Plantilla: archivos Excel descargables gratuitamente

## Tecnologías utilizadas
- Python
- Django
- Bootstrap 5
- SQLite