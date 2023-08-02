from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Articulo
from django.views import View
from .forms import ArticuloForm
from apps.comentario.forms import ComentarioForm
from apps.comentario.models import Comentario
from .models import Articulo, Categoria
from django.http import HttpResponse
from io import BytesIO
from xhtml2pdf import pisa
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from .models import Calificacion
from django.db.models import Avg
import logging

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

        # Renderizamos la plantilla HTML si no se solicita la descarga del PDF
        if not categoria_id:
            return render(request, 'articulos/articulo.html', {'articulos': articulos, 'categorias': categorias, 'categoria_id': categoria_id})

        # Supongamos que se generó el archivo PDF en 'articulos.pdf'
        pdf_file_path = 'articulos.pdf'

        # Abre el archivo PDF y devuelve su contenido como una respuesta
        with open(pdf_file_path, 'rb') as pdf_file:
            response = HttpResponse(pdf_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="articulo_{categoria_id}.pdf"'
            return response

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

def eliminar_articulo(request,articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)

    if request.method == 'POST':
        articulo.delete()
        return redirect('apps.articulo:articulos')
    return render(request, 'articulos/eliminar_articulo.html', {'articulo': articulo})

def descargar_pdf(request, articulo_id):
    # Obtener el artículo específico
    articulo = get_object_or_404(Articulo, id=articulo_id)

    # Obtener el contenido del template del PDF
    template = get_template('articulos/articulo_pdf.html')
    context = {'articulos': articulo}
    html = template.render(context)

    # Crear el archivo PDF
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)

    # Verificar si se generó correctamente el PDF
    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{articulo.titulo}.pdf"'
        return response

    return HttpResponse("Error al generar el PDF", status=500)

    
    
@login_required
def calificar_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, id=articulo_id)

    if request.method == 'POST':
        valor = request.POST.get('valor')
        # Asegúrate de validar que 'valor' tenga un valor válido antes de guardar la calificación
        if valor is not None and valor.isdigit():
            valor = int(valor)

            # Crear una instancia de Calificacion y guardarla en la base de datos
            calificacion, created = Calificacion.objects.get_or_create(
                articulo=articulo,
                usuario=request.user,
                defaults={'valor': valor}
            )

            # Si la calificación ya existía, actualizamos el valor
            if not created:
                calificacion.valor = valor
                calificacion.save()

            # Recalculamos la calificación promedio del artículo
            calificacion_promedio = Calificacion.objects.filter(articulo=articulo).aggregate(Avg('valor'))['valor__avg']
            if calificacion_promedio is not None:
                articulo.calificacion_promedio = round(calificacion_promedio, 2)
                articulo.save()

            # Redirigir al usuario a la página de detalles del artículo
            return redirect(reverse('apps.articulo:leer_articulo', kwargs={'id': articulo_id}))

    return render(request, 'articulos/articulo_individual.html', {'articulos': articulo})

def carrusel_view(request):
    # Obtener los tres mejores artículos ordenados por calificacion_promedio en orden descendente
    articulos = Articulo.objects.all()
    articulos = Articulo.objects.order_by('-calificacion_promedio')[:3]

    # Imprimir los atributos de cada artículo en la consola
    for articulo in articulos:
        print("Título:", articulo.titulo)
        print("Resumen:", articulo.resumen)
        print("Calificación promedio:", articulo.calificacion_promedio)
        print("---")

    # Pasar los tres mejores artículos al contexto y renderizar la plantilla base.html
    return render(request, 'base.html', {'mejores_articulos': articulos})

