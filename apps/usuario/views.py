from .forms import RegistroUsusarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth import logout,login
from apps.usuario.models import Usuario
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.views import PasswordResetView
from smtplib import SMTPAuthenticationError
from .forms import CustomUserUpdateForm
from django.views.decorators.csrf import csrf_exempt

class RegistrarUsuario(CreateView):
    template_name = 'registration/registrar.html'
    form_class = RegistroUsusarioForm

    def get(self, request, *args, **kwargs):
        # Obtener la URL de la página a la que se redirigirá después del registro
        self.next_page = request.GET.get('next')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        miembro_group = Group.objects.get(name='Miembro')
        self.object.groups.add(miembro_group)

        # Autenticar al usuario recién registrado
        login(self.request, self.object)

        return JsonResponse({'success': True, 'next_page': self.next_page})

    def form_invalid(self, form):
        return JsonResponse({'success': False, 'message': 'Error al intentar registrarse', 'errors': form.errors})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next_page'] = self.next_page
        return context
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
@login_required
def user_update_view(request):
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        form = CustomUserUpdateForm(instance=request.user)

    return render(request, 'registration/modificar_usuario.html', {'form': form})
@csrf_exempt
def save_next_page(request):
    if request.method == 'POST':
        next_page = request.POST.get('next_page')
        request.session['next_page'] = next_page
        return JsonResponse({})
    return JsonResponse({}, status=400)