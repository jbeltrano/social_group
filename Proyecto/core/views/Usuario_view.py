from django.shortcuts import render
from core.controllers import Controlador_usuario

def lista_usuarios_view(request):
    usuarios = Controlador_usuario.obtener_todos_usuarios()
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})

