
from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('',views.home,name='home'),
    path('buscar-mascotas/',views.buscar_mascotas,name = 'buscar_mascotas'),
    path('crear-mascotas/',views.crear_mascotas,name = 'crear_mascotas'),
    path('about-me/',views.about_me,name = 'about_me'),
    path('ver-mascota/<int:id>/',views.ver_mascota,name = 'ver_mascota'),
    path('eliminar-mascota/<int:id>/',views.eliminar_mascota,name = 'eliminar_mascota'),
    path('editar-mascota/<int:id>/',views.editar_mascota,name = 'editar_mascota'),
]