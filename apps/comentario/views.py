from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Comentario
from .forms import ComentarioForm
from django.views.generic import DeleteView
from apps.usuario.models import Usuario
from django.urls import reverse_lazy
from apps.articulo.models import Articulo

# Create your views here.

@login_required
def comentar(request, id):
    articulo = get_object_or_404(Articulo, id=id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.articulo = articulo
            comentario.usuario = request.user
            comentario.save()
            return redirect('leer_articulo', id=id)
    else:
        form = ComentarioForm()
    return render(request, 'comentario/comentar.html', {'form' : form, 'articulo' : articulo})
    

def listado_comentario(request):
    comentarios = Comentario.objects.all()
    usuario = request.user.id

    context = {
        'comentarios' : comentarios,
        'usuario' : usuario
    }
    return render(request, 'comentario/listadoComentario.html', context)

def agregarComentario(request, id):
    if request.method == "POST":
        form = ComentarioForm(data = request.POST)
        form.instance.usuario = request.user
        articulo = Articulo.objects.get(id=id)
        form.instance.articulo = articulo
        if form.is_valid():
            form.save()
        else:
            return redirect('apps.articulo:leer_articulo', id, { 'comment_form': form})
    return redirect('apps.articulo:leer_articulo', id)


class DeleteComentario(DeleteView):
    model = Comentario
    template_name = 'comentario/eliminarComentario.html'
    success_url = reverse_lazy('apps.articulo:articulos')



def detalle_articulo(request, articulo_id):
    articulo = Articulo.objects.get(id=articulo_id)
    comentario = Comentario.objects.filter(articulo=articulo)
    return render(request, 'detalle_articulo.html', {'articulo' : articulo, 'comentario' : comentario})