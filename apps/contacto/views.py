from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from .forms import ContactoForm
from django.urls import reverse_lazy


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