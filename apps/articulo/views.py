from django.shortcuts import render, get_object_or_404, redirect
from .models import Articulo
from django.views import View
from .models import Noticia
from .forms import NoticiaForm
from .forms import ArticuloForm

#vista basada en funcion 

# def articulos(request):
#     articulos = Articulo.objects.all()
#     return render(request, 'articulo.html', {'articulos' : articulos})

# #vista basada en clases

class ArticuloView(View):
    template_name = 'articulos/articulo.html'

    def get(self, request):
        articulos = Articulo.objects.all()
        return render(request, 'articulos/articulo.html', {'articulos' : articulos})


def existe_articulo(id):
    for i in Articulo:
        if i.id == id:
            return None
        
def leer_articulo(request, id):       
    try:
        articulos = existe_articulo(id)

    except Exception:
        articulos = Articulo.objects.get(id = id)

        context = {
            'articulos' : articulos
        }

    return render(request, 'articulos/articulo_individual.html', context)

## Agrego lo relacionado con el desafío para crear noticias
def crear_noticia(request):
    if request.method == 'POST':
        # Para datos del formulario y guardar nuevas noticias en B.datos
        pass
    else:
        # Mostrar el form para nueva noticia
        return render(request, 'crear_noticia.html')

def registro_noticias(request): # Ver bien el nombre plisss
    noticias = Noticia.objects.all().order_by('-fecha_publicacion')
    return render(request, 'registro_noticias.html', {'noticias': noticias})

# para actualizar o editar noticias
def editar_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    # se emplea la función get_object_or_404 para obtener la noticia existente 
    # según su ID. después, se verifica si la solicitud es de tipo POST. 
    # Si es así, se valida el formulario y, si es válido, los cambios se guardan en BD
    #  y va a la lista de noticias

    if request.method == 'POST':
        form = NoticiaForm(request.POST, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('registro_noticias')
    else:
        form = NoticiaForm(instance=noticia)

    return render(request, 'editar_noticia.html', {'form': form})

# para eliminar una noticia se verifica si la solicitud es de tipo POST.
#  Si es así, se elimina la noticia utilizando el método delete() y después
#  se redirige a la lista de noticias.
def detalle_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)

    if request.method == 'POST':
        noticia.delete()
        return redirect('lista_noticias')

    return render(request, 'detalle_noticia.html', {'noticia': noticia})

# Para secciones adicionales como piden en el desafío

def inicio(request):
    return render(request, 'inicio.html')

def categorias(request):
    return render(request, 'categorias.html')

def acerca_de(request):
    return render(request, 'acercade/acercade.html')

def contacto(request):
    return render(request, 'contacto.html')
def modificar(request,id):
    articulos = Articulo.objects.get(id=id)
    formulario = ArticuloForm(request.POST or None, request.FILES or None, instance=articulos)
    
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('apps.articulo:articulos')
    
    return render(request, 'articulos/modificar.html', {'formulario':formulario})