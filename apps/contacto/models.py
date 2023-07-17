from django.db import models
from django.utils import timezone

class Contacto(models.Model):
    nombre_apellido = models.CharField(max_length=120, null=False)
    email = models.EmailField()
    asunto = models.CharField(max_length=50)
    mensaje = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)

    def __srt__(self):
        return self.nombre_apellido

