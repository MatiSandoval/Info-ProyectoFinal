from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from .forms import ContactoForm
from django.urls import reverse_lazy
# from django.contrib import messages
# Create your views here.


# class ContactoUsuario(CreateView):
#     template_name = 'contacto.html'
#     form_class = ContactoForm
#     success_url = reverse_lazy('index')

#     def form_valid(self, form):
#         messages.success('')
#         return super().form_valid(form)
#vista en class 

def contacto(request):
    data = {'form': ContactoForm()}

    if request.method == 'POST':
        formulario = ContactoForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Mensaje enviado'
        else:
            data ['form'] = formulario
            
    return render(request, 'contacto/contacto.html', data)