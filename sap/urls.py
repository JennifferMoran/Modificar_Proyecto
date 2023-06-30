"""
URL configuration for sap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from citasmd.views import  agregar_citasmd, ver_citasmd, editar_citasmd, eliminar_citasmd, generar_reporte
from webapp.views import  mostrar_citasmd

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mostrar_citasmd, name='inicio'),
    path('agregar_citasmd/', agregar_citasmd),
    path('ver_citasmd/<int:idCitasMd>', ver_citasmd),
    path('editar_citasmd/<int:idCitasMd>', editar_citasmd),
    path('eliminar_citasmd/<int:idCitasMd>', eliminar_citasmd),
    path('generar_reporte/', generar_reporte),
]