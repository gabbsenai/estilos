from django import forms
from .models import Musica

class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = ['nome', 'estilo']
        