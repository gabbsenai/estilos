from django.urls import path
from estilos.views import cadastrar_estilos, editar_estilos, excluir_estilos, listar_estilos

urlpatterns = [
    path('', listar_estilos, name='listar_estilos'),
    path('cadastrar/', cadastrar_estilos, name='cadastrar_estilos'),
    path('editar/<int:id>/', editar_estilos, name='editar_estilos'),
    path('excluir/<int:id>/', excluir_estilos, name='excluir_estilos'),
]