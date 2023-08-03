from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import authenticate, login, get_user_model
from django.forms.widgets import ClearableFileInput

class RegistroUsusarioForm(UserCreationForm):
 
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'email', 'imagen']
    

    class LoginForm(forms.Form):
        username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingUsername', 'placeholder': 'Nombre de Usuario'}))
        password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'floatingPassword', 'placeholder': 'Contraseña'}))
        
        def login(self, request):
            username = self.cleaned_data.get('username')
            password = self.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
CustomUser = get_user_model()

class CustomUserUpdateForm(forms.ModelForm):
    imagen = forms.ImageField(required=False, widget=forms.FileInput)  # Eliminar el atributo "clearable" para evitar la opción de eliminar

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'imagen']