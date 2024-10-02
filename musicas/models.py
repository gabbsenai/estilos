from django.db import models
from estilos.models import Estilos


class Musica(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    estilo = models.ForeignKey(Estilos, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.nome
