from django.urls import path
# froarticulosm .views import  Importacion para funcion
from .views import ArticuloView
from . import views

app_name = 'apps.articulo'

urlpatterns = [
    # path('articulos/', articulos, name = 'articulos'), #forma para definir funcion
    path('articulos/', ArticuloView.as_view(), name = 'articulos'),
    path('leer_articulo/<int:id>', views.leer_articulo, name = 'leer_articulo'),
    path('crear-noticia/', views.crear_noticia, name='crear_noticia'),
    path('noticias/', views.registro_noticias, name='registro_noticias'),
    path('editar-noticia/<int:noticia_id>/', views.editar_noticia, name='editar_noticia'),
    path('noticias/<int:noticia_id>/', views.detalle_noticia, name='detalle_noticia'),
    path('', views.inicio, name='inicio'),
    path('categorias/', views.categorias, name='categorias'),
    path('acerca_de/', views.acerca_de, name='acerca_de'),
    path('contacto/', views.contacto, name='contacto'),
    path('modificar/',views.modificar, name='modificar'),
    path('modificar/<int:id>',views.modificar, name='modificar'),
    path('existe_articulo/', views.existe_articulo, name='existe_articulo'),
    path('articulo_crear/', views.articulo_crear, name='articulo_crear'),

]
 