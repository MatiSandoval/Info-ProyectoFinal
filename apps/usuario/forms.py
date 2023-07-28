from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import authenticate, login


class RegistroUsusarioForm(UserCreationForm):
 
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'email', 'imagen']
    

    class LoginForm(forms.Form):
        username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}))
        password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
        
        def login(self, request):
            username = self.cleaned_data.get('username')
            password = self.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
    