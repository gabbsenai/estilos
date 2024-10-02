from django.shortcuts import get_object_or_404, redirect, render
from estilos.models import Estilos

def listar_estilos(request):
    estilos = Estilos.objects.all()
    return render(request, 'listarestilos.html', {'estilos':estilos})

def cadastrar_estilos(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        Estilos.objects.create(nome=nome,)
        return redirect('listar_estilos')
    return render(request, 'formestilo.html')

def editar_estilos(request, id):
    estilos = get_object_or_404(Estilos, id=id)
    if request.method == 'POST':
        estilos.nome = request.POST['nome']
        estilos.save()
        return redirect('listar_estilos')
    return render(request, 'formestilo.html', {'estilos': estilos})

def excluir_estilos(request, id):
    estilos = get_object_or_404(Estilos, id=id)
    if request.method == 'POST':
        estilos.delete()
        return redirect('listar_estilos')
    return render(request, 'confirmar_ex_estilo.html', {'estilos':estilos})
