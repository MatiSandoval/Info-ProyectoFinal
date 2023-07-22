from .forms import RegistroUsusarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.

class RegistrarUsuario(CreateView):
    template_name = 'registration/registrar.html'
    form_class = RegistroUsusarioForm
    
    def form_valid(self, form):
        messages.success(self.request, 'Registro exitoso. Por favor, inicia sesión.')
        form.save()
        next_url = self.request.GET.get('next')
        if next_url:
            self.request.session['next'] = next_url
            
        return redirect('apps.usuario:login')
    
class LoginUsuario(LoginView):
    template_name = 'registration/login.html'
        
    def get_success_url(self):
        next_url = self.request.GET.get('next') or self.request.session.get('next')
        if next_url:
            self.request.session.pop('next', None)
            messages.success(self.request, 'Login exitoso')
            return next_url
        else:
            messages.success(self.request, 'Login exitoso')
                
            return reverse('index')
        
class LogoutUsuario(LogoutView):
    template_name = 'registration/logout.html'
        
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.success(request, 'Logout exitoso.')
        return response
        
    def get_next_page(self):
        return reverse('login')