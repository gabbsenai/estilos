from django.db import models

class Estilos(models.Model):
    nome = models.CharField(max_length=75, null=False, blank=False)

    def __str__(self) -> str:
        return self.nome
