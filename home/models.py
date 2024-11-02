from django.db import models
from django.utils import timezone

class Mascota(models.Model): 
    nombre =  models.CharField(max_length=20)
    especie = models.CharField(max_length=20)
    edad = models.IntegerField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_edicion = models.DateTimeField(default=timezone.now)
    autor = models.CharField(max_length=100, default='Sin-Autor')
    
    
    def __str__(self):
        return f'{self.id}: {self.especie} -> {self.nombre}, {self.edad} años.'
    
class DatosExtra(models.Model):
    mascota = models.OneToOneField(Mascota,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='mascotas',blank=True,null=True, default='mascotas/default-image.jpg')