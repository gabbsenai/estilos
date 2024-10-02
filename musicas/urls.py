from django.urls import path
from musicas.views import cadastrar_musica, editar_musica, excluir_musica, listar_musicas

urlpatterns = [
    path('', listar_musicas, name='listar_musicas'),
    path('musicas/cadastrar/', cadastrar_musica, name = 'cadastrar_musica'),
    path('musicas/editar/<int:id>/', editar_musica, name='editar_musica'),
    path('musicas/excluir/<int:id>/', excluir_musica, name='excluir_musica'),
]
