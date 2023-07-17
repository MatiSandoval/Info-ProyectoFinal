from django.urls import path
# froarticulosm .views import  Importacion para funcion
from .views import ArticuloView
from . import views

app_name = 'apps.articulo'

urlpatterns = [
    # path('articulos/', articulos, name = 'articulos'), #forma para definir funcion
    path('articulos/', ArticuloView.as_view(), name = 'articulos'),
    path('leer_articulo/<int:id>', views.leer_articulo, name = 'leer_articulo'),
]
 