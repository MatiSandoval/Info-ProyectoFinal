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
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        miembro_group = Group.objects.get(name='Miembro')
        self.object.groups.add(miembro_group)
        login(self.request, self.object)

        return JsonResponse({'success': True, 'next_page': self.success_url})

    def form_invalid(self, form):
        return JsonResponse({'success': False, 'message': 'Error al intentar registrarse', 'errors': form.errors})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next_page'] = self.success_url
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
    user = request.user
    miembro_group = Group.objects.get(name='Miembro')
    colaborador_group = Group.objects.get(name='Colaborador')
    if user.groups.filter(name='Miembro').exists():
        user.groups.remove(miembro_group)
        user.groups.add(colaborador_group)
        response_data = {
            'success': True,
            'message': 'Ahora eres un colaborador.',
        }
    else:
        response_data = {
            'success': False,
            'message': 'El usuario no es miembro.',
        }

    return JsonResponse(response_data)

class CustomPasswordResetView(PasswordResetView):
    def form_valid(self, form):
        try:
            user = Usuario.objects.get(email=form.cleaned_data['email'])
        except ObjectDoesNotExist:
            form.add_error('email', 'El correo electrónico no está registrado en nuestro sistema.')
            return super().form_invalid(form)

        try:
            response = super().form_valid(form)
            return response
        except SMTPAuthenticationError as e:
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