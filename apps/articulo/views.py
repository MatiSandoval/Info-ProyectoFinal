from django.shortcuts import render
from .models import Articulo
from django.views import View
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
