# Finanzas Claras

Web de consultoría financiera para Pymes y personas, desarrollada con Django.

## Descripción
Finanzas Claras es una plataforma web que ofrece servicios de asesoramiento 
financiero para Pymes y personas con poca experiencia en finanzas personales. 
Incluye un blog, tutoriales en video y plantillas gratuitas descargables.

## Requisitos
- Python 3.x
- Django 6.x

## Instalación
1. Clonar el repositorio
2. Instalar Django: pip install django
3. Ejecutar migraciones: python manage.py migrate
4. Iniciar servidor: python manage.py runserver

## Orden para probar las funcionalidades
1. Ir a /servicios para ver y cargar servicios
2. Ir a /blog para ver y cargar artículos
3. Ir a /tutoriales para ver y cargar tutoriales
4. Ir a /plantillas para ver y cargar plantillas
5. Ir a /contacto para registrar un cliente
6. Ir a /buscar-cliente para buscar clientes registrados

## Modelos
- Servicio: servicios ofrecidos por Finanzas Claras
- Articulo: publicaciones del blog
- Cliente: personas que contactan para contratar servicios
- Tutorial: videos cortos sobre finanzas
- Plantilla: archivos Excel descargables gratuitamente