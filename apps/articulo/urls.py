from django.urls import path
from .views import ArticuloView, descargar_pdf,carrusel_view
from . import views

app_name = 'apps.articulo'

urlpatterns = [
    path('articulos/', ArticuloView.as_view(), name = 'articulos'),
    path('articulos/<str:categorias>', ArticuloView.as_view(), name = 'articulos_por_categoria'),
    path('leer_articulo/<int:id>', views.leer_articulo, name = 'leer_articulo'),
    path('modificar/',views.modificar, name='modificar'),
    path('modificar/<int:id>',views.modificar, name='modificar'),
    path('existe_articulo/', views.existe_articulo, name='existe_articulo'),
    path('articulo_crear/', views.articulo_crear, name='articulo_crear'),
    path('acerca_de/', views.acerca_de, name='acerca_de'),
    path('articulos/<int:articulo_id>/descargar/', descargar_pdf, name='descargar_pdf'),
    path('calificar/<int:articulo_id>/', views.calificar_articulo, name='calificar_articulo'),
    path('eliminar_articulo/<int:articulo_id>/', views.eliminar_articulo, name='eliminar_articulo'),
]
 