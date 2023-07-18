from django import forms
from .models import Noticia

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'contenido', 'fecha_publicacion']

#los campos tenemos que definirlos de acuerdo a nuestras necesidades
class MiFormulario(forms.Form):
    campo1 = forms.CharField(label='Campo 1', max_length=100)
    campo2 = forms.IntegerField(label='Campo 2')
    campo3 = forms.BooleanField(label='Campo 3')
