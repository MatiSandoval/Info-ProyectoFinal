from django.db import models
from django.utils import timezone

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=80, null=False)
    apellido = models.CharField(max_length=80, null=False)
    telefono = models.IntegerField()
    username = models.CharField(max_length=120, null=False)
    email = models.EmailField(max_length=250, null=False)
    contraseña = models.CharField(max_length=50, null=False)
    fecha_registro = models.DateTimeField(default=timezone.now)
    avatar = models.ImageField(null=True, blank=True, upload_to='usuario', default='articulo/default.png')
    estado = models.BooleanField(default=True)

    class Meta:
        ordering = ('-nombre',)

    def __str__(self):
        return self.nombre
  
    def delete(self, using=None, keep_parents= False):
        self.imagen.delete(self.imagen.name)
        super().delete()