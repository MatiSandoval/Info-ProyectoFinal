from django.db import models
from django.utils import timezone

#Create your models here.

class Articulo(models.Model):
    titulo = models.CharField(max_length=30, null= False)
    resumen = models.TextField(null=False)
    contenido = models.TextField(null=False)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(null=True, blank=True, upload_to='articulo', default='articulo/default.jpg')
    estado = models.BooleanField(default=True)
    publicado = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-publicado',)

    def __str__(self):
        return self.titulo
  
    def delete(self, using=None, keep_parents= False):
        self.imagen.delete(self.imagen.name)
        super().delete()

class Noticia(models.Model):
    titulo = models.CharField(max_length=30, null= False)
    resumen = models.TextField(null=False)
    contenido = models.TextField(null=False)
    fecha_publicacion = models.DateTimeField(auto_now_add=False)
    imagen = models.ImageField(null=True, blank=True, upload_to='articulo', default='articulo/default.jpg')
    estado = models.BooleanField(default=True)
    publicado = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-titulo',)

    def __str__(self):
        return self.titulo
  
