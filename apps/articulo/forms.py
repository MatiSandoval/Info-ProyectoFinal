from django import forms
from .models import Articulo


    

class ArticuloForm(forms.ModelForm):
    imagen = forms.ImageField(required=False, widget=forms.FileInput(attrs={'clearable': False}))

    class Meta:
        model = Articulo
        fields = ['titulo', 'resumen', 'contenido', 'imagen', 'categoria']
        widgets = {
            'resumen': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),
        }
