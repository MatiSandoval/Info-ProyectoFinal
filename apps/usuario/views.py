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
from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.views import PasswordResetView
from smtplib import SMTPAuthenticationError


class RegistrarUsuario(CreateView):
    template_name = 'registration/registrar.html'
    form_class = RegistroUsusarioForm
    
    def form_valid(self, form):
        response = super().form_valid(form)
        miembro_group = Group.objects.get(name='Miembro')
        self.object.groups.add(miembro_group)
        data = {'success': True, 'message': ''}
        return JsonResponse(data)

    def form_invalid(self, form):
        data = {'success': False, 'message': ''}
        return JsonResponse(data)
class LoginUsuario(LoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
        messages.success(self.request, '')
        return super().form_valid(form)
        



class LogoutUsuario(LogoutView):
    template_name = 'registration/logout.html'
        
    def dispatch(self, request, *args, **kwargs):
        try:
            logout(request)
            response_data = {
                'success': True,
                'message': ''
            }
        except Exception as e:
            response_data = {
                'success': False,
                'message': ''
            }
        return JsonResponse(response_data)
    
@login_required
def profile(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'profile.html', context)

@login_required
def ser_colaborador(request):
    # Obtener el usuario actual que hizo clic en el botón "Ser Colaborador"
    user = request.user

    # Obtener los grupos "Miembro" y "Colaborador"
    miembro_group = Group.objects.get(name='Miembro')
    colaborador_group = Group.objects.get(name='Colaborador')

    # Verificar si el usuario ya es miembro antes de proceder
    if user.groups.filter(name='Miembro').exists():
        # Remover al usuario del grupo "Miembro"
        user.groups.remove(miembro_group)

        # Asignar al usuario al grupo "Colaborador"
        user.groups.add(colaborador_group)

        # Devolver una respuesta JSON para indicar que el usuario se ha vuelto colaborador
        response_data = {
            'success': True,
            'message': 'Ahora eres un colaborador.',
        }
    else:
        # Si el usuario no es miembro, no se realiza ninguna acción.
        response_data = {
            'success': False,
            'message': 'El usuario no es miembro.',
        }

    return JsonResponse(response_data)

class CustomPasswordResetView(PasswordResetView):
    def form_valid(self, form):
        try:
            # Verificar si el correo electrónico proporcionado está asociado a un usuario
            user = Usuario.objects.get(email=form.cleaned_data['email'])
        except ObjectDoesNotExist:
            # Si el correo electrónico no está asociado a un usuario, mostrar un mensaje de error
            form.add_error('email', 'El correo electrónico no está registrado en nuestro sistema.')
            return super().form_invalid(form)

        try:
            # Intentar enviar el correo de restablecimiento de contraseña
            response = super().form_valid(form)
            return response
        except SMTPAuthenticationError as e:
            # Si ocurre un error SMTP (por ejemplo, credenciales incorrectas),
            # mostrar un mensaje de error en el formulario
            form.add_error(None, 'Ocurrió un error al enviar el correo. Por favor, inténtalo de nuevo más tarde.')
            return super().form_invalid(form)