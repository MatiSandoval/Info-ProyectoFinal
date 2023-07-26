from django import forms
from .models import Articulo


#los campos tenemos que definirlos de acuerdo a nuestras necesidades
class MiFormulario(forms.Form):
    campo1 = forms.CharField(label='Campo 1', max_length=100)
    campo2 = forms.IntegerField(label='Campo 2')
    campo3 = forms.BooleanField(label='Campo 3')
    

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'resumen', 'contenido', 'imagen', 'estado', 'categoria']
