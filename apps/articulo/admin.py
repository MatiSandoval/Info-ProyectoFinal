from django.contrib import admin
from .models import Categoria, Articulo, Calificacion 


@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin): 
    list_display = ('id','titulo', 'resumen', 'contenido', 'fecha_publicacion', 'imagen', 'estado', 'categoria', 'publicado')

admin.site.register(Categoria) 
admin.site.register(Calificacion) 