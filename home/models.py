from django.db import models

class Mascota(models.Model): 
    nombre =  models.CharField(max_length=20)
    especie = models.CharField(max_length=20)
    edad = models.IntegerField()