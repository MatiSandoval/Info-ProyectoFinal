from django.urls import path
from . import views


app_name = 'apps.comentario'

urlpatterns = [
    path('comentar/<int:id>', views.comentar , name="comentar"),
    path('agregarComentario/<int:id>',  views.agregarComentario, name="agregarComentario"),
    path('listado_comentario/', views.listado_comentario, name='listado_comentario'),
    path('detalle/', views.detalle_articulo, name='detalle'),
    path('eliminarComentario/<pk>', views.DeleteComentario.as_view(), name='eliminarComentario'),
    path('editar_comentario/<int:comentario_id>/', views.editar_comentario, name='editar_comentario'),

]