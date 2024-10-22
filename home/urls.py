
from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('',views.home,name='home'),
    path('buscar-mascotas',views.buscar_mascotas,name = 'buscar_mascotas'),
    path('crear-mascotas',views.crear_mascotas,name = 'crear_mascotas')

]