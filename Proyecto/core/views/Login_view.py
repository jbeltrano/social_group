from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from core.controllers import Controlador_usuario
from core.controllers import Controlador_login
from core.models.Usuario import Usuario
from functools import wraps

def login_requerido(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if "usuario_id" not in request.session:
            return redirect("login")
        return func(request, *args, **kwargs)
    return wrapper


def login_view(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        error = Controlador_login.verificar_login(username, password)

        if error:
            messages.error(request, error)
            return render(request, "login/login.html")
        
        usuario = Controlador_usuario.obtener_usuario(correo=username)
        Controlador_login.iniciar_sesion(request, usuario)
        next_url = request.POST.get("next") or "/"
        print(request.POST.get("next"))
        return redirect(next_url)
        
    return render(request, "login/login.html")


def logout_view(request):

    request.session.flush()  # Elimina toda la información de sesión
    messages.success(request, "Has cerrado sesión exitosamente")
    return redirect("lista_recetas")


def registro_view(request):

    if request.method == "POST":

        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        correo = request.POST.get("correo")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        errores = Controlador_login.verificar_registro(nombre, apellido, correo, password, confirm_password)

        if errores:
            for mensaje in errores:
                messages.error(request, mensaje)
            return render(request, "login/registro.html")
        
        if Controlador_usuario.usuario_existe(correo):
            messages.error(request, "Este correo electrónico ya está registrado")
            return render(request, "login/registro.html")

          
        # Crear el usuario
        usuario = Controlador_usuario.insertar_usuario(
            correo=correo,
            nombre=f"{nombre} {apellido}",
            contraseña=password
        )
        
        # Iniciar sesión automáticamente
        Controlador_login.iniciar_sesion(request, usuario)
        
        messages.success(request, "Cuenta creada exitosamente")
        next_url = request.POST.get("next") or "/"
        return redirect(next_url)

    return render(request, "login/registro.html")
