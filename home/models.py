from django.db import models

class Mascota(models.Model): 
    nombre =  models.CharField(max_length=20)
    especie = models.CharField(max_length=20)
    edad = models.IntegerField()
    
    def __str__(self):
        return f'{self.id}: {self.especie} -> {self.nombre}, {self.edad} años.'