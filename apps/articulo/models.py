from typing import Any, Dict, Tuple
from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy
from django.conf import settings

#Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=60, null=False)
    
    def __str__(self):
        return self.nombre 


class Articulo(models.Model):
    titulo = models.CharField(max_length=100, null= False)
    resumen = models.TextField(null=False)
    contenido = models.TextField(null=False)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(null=True, blank=True, upload_to='articulo', default='articulo/imagen.jpg')
    estado = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default='Sin categoria')
    publicado = models.DateTimeField(default=timezone.now)
    calificacion_promedio = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)

    class Meta:
        ordering = ('-publicado',)

    def __str__(self):
        return self.titulo
  
    def delete(self, using=None, keep_parents= False):
        self.imagen.delete(self.imagen.name)
        super().delete()
        
    def get_link_comentar(self):
        return reverse_lazy('apps.comentario:agregarComentario', args=[self.id])

class Calificacion(models.Model):
    articulo = models.ForeignKey('articulo.Articulo', on_delete=models.CASCADE, related_name= 'calificacion')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='calificacion')
    valor = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1)

    class Meta:
        unique_together = ('articulo', 'usuario')   