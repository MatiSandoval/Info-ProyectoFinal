from django.shortcuts import render, get_object_or_404, redirect
from .models import Articulo
from django.views import View
from .forms import ArticuloForm
from apps.comentario.forms import ComentarioForm
from apps.comentario.models import Comentario
from .models import Articulo, Categoria

class ArticuloView(View):
    template_name = 'articulos/articulo.html'

    def get(self, request, categorias=None, categoria_id=None, orden=None, fecha=None):
        orden = request.GET.get('orden')
        fecha = request.GET.get('fecha')
        categoria_id = request.GET.get('categoria')
        
        print('fecha:', fecha)

        # Obtenemos todos los artículos y los ordenamos según el criterio seleccionado
        articulos = Articulo.objects.all()

        if orden == 'ascendente':
            articulos = articulos.order_by('titulo')
        elif orden == 'descendente':
            articulos = articulos.order_by('-titulo')

        if fecha == 'ascendente':
            articulos = articulos.order_by('fecha_publicacion')
        elif fecha == 'descendente':
            articulos = articulos.order_by('-fecha_publicacion')

        # Si se proporciona el parámetro 'categorias', filtramos los artículos por la categoría seleccionada
        if categorias is not None and categorias.isdigit() and categorias != '0':
            
            categorias = int(categorias)  # Convertimos 'categorias' a un número entero
            articulos = articulos.filter(categoria=categorias)

        # Obtenemos todas las categorías para mostrarlas en el filtro
        categorias = Categoria.objects.all()

        return render(request, 'articulos/articulo.html', {'articulos': articulos, 'categorias': categorias,'categoria_id': categoria_id})


def existe_articulo(id):
    for i in Articulo:
        if i.id == id:
            return None
        
def leer_articulo(request, id):       
    try:
        articulos = existe_articulo(id)

    except Exception:
        articulos = Articulo.objects.get(id=id)
        comentarios = Comentario.objects.filter(articulo=id)

    form = ComentarioForm(request.POST or None)
    if form.is_valid():
        print(f"Form is valid: {form.is_valid()}")
        if not form.is_valid():
            print(form.errors)
        if request.user.is_authenticated:
            aux = form.save(commit=False)
            aux.articulo = articulos
            aux.usuario = request.user
            aux.save()
            form = ComentarioForm()

        else:
            return redirect('usuario:login')

    context = {
        'articulos' : articulos,
        'form': form,
        'comentarios' : comentarios,
    }

    return render(request, 'articulos/articulo_individual.html', context)

def articulo_crear(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            print(f'Form is valid: {form.is_valid()}')
            form.save()
            return redirect('apps.articulo:articulos')
    else:
        form = ArticuloForm()
    return render(request, 'articulos/articulo_form.html', {'form': form})

def articulo_actualizar(request, pk):
    articulo = get_object_or_404(Articulo, pk = pk)
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES, instance=articulo)
        if form.is_valid():
            form.save
            return redirect('articulos')
        
    else:
        form = ArticuloForm(instance=articulo)
    return render(request, 'articulos/articulo_form.html', {'form':form})
        
def acerca_de(request):
    return render(request, 'acercade/acercade.html')

def modificar(request,id):
    articulos = Articulo.objects.get(id=id)
    formulario = ArticuloForm(request.POST or None, request.FILES or None, instance=articulos)
    
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('apps.articulo:articulos')
    
    return render(request, 'articulos/modificar.html', {'formulario':formulario})

