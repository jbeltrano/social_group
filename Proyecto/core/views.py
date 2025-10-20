from django.shortcuts import render
from .models import Usuario

def lista_usuarios_view(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})

def boton_usuario_view(request):
    return render(request, 'usuarios/boton_usuario.html')
