from .forms import RegistroUsusarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth import logout
from apps.usuario.models import Usuario
from django.shortcuts import render
from django.contrib.auth.decorators import login_required



class RegistrarUsuario(CreateView):
    template_name = 'registration/registrar.html'
    form_class = RegistroUsusarioForm
    
    def form_valid(self, form):
        response = super().form_valid(form)
        data = {'success': True, 'message': 'Registro exitoso. Por favor, inicia sesión.'}
        return JsonResponse(data)

    def form_invalid(self, form):
        data = {'success': False, 'message': 'Error al registrar. Por favor, corrija los errores e intente nuevamente.'}
        return JsonResponse(data)
class LoginUsuario(LoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
        messages.success(self.request, 'Login exitoso')
        return super().form_valid(form)
        



class LogoutUsuario(LogoutView):
    template_name = 'registration/logout.html'
        
    def dispatch(self, request, *args, **kwargs):
        try:
            logout(request)
            response_data = {
                'success': True,
                'message': 'Logout exitoso. ¡Hasta luego!'
            }
        except Exception as e:
            response_data = {
                'success': False,
                'message': 'Error al hacer logout. Por favor, inténtelo nuevamente.'
            }
        return JsonResponse(response_data)
    
@login_required
def profile(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'profile.html', context)