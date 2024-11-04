from django.db import models
from django.contrib.auth.models import User

class ChatPublico(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    mensaje = models.TextField()
    horario_envio = models.DateTimeField(auto_now_add=True)

