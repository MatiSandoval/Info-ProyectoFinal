from django.contrib import admin
from .models import Contacto #Importo las clases o medelos

# Register your models here.

@admin.register(Contacto)
class ArticuloAdmin(admin.ModelAdmin): 
    list_display = ('id','nombre_apellido', 'email', 'asunto', 'fecha')
