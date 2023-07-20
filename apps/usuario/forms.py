from django import forms
from .models import Usuario

class UsusarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = {
        'contraseña': forms.PasswordInput(),
    }