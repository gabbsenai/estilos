from django.shortcuts import get_object_or_404, redirect, render
from musicas.forms import MusicaForm
from musicas.models import Musica

def listar_musicas(request):
    musicas = Musica.objects.all()
    return render(request, 'listarmusica.html', {'musicas':musicas })

def cadastrar_musica(request):
    form = MusicaForm(request.POST) if request.method == "POST" else MusicaForm()
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('listar_musicas')
    return render(request, 'formmusica.html', {'form':form})

def editar_musica(request, id):
    musica = get_object_or_404(Musica, id=id)
    if request.method == 'POST':
        form = MusicaForm(request.POST, instance=musica)
        if form.is_valid():
            form.save()
            return redirect('listar_musicas')
    else:
        form = MusicaForm(instance=musica)
        return render(request, 'formmusica.html', {'form': form})
    
def excluir_musica(request, id):
    musica = get_object_or_404(Musica, id=id)
    if request.method == "POST":
        musica.delete()
        return redirect('listar_musicas')
    return render(request, 'confirmar_ex_musica.html', {'musica':musica})
