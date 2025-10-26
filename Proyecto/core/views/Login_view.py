from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from core.controllers import Controlador_usuario
from core.models.Usuario import Usuario


def login_requerido(func):

    def wrapper(request, *args, **kwargs):

        if "usuario_id" not in request.session:
            return redirect("login")
        
        return func(request, *args, **kwargs)
    
    return wrapper


def login_view(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        try:
            usuario = Controlador_usuario.obtener_usuario(correo=username)

            if Controlador_usuario.verificar_contraseña(usuario=usuario, contraseña=password):

                request.session["usuario_id"] = usuario.correo
                request.session["usuario_nombre"] = usuario.nombre

                messages.success(request, "Inicio de sesión exitoso")
                return redirect("lista_recetas")
            
            else:
                messages.error(request, "Contraseña incorrecta")

        except Usuario.DoesNotExist:
            messages.error(request, "Usuario no encontrado")

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

        # Validaciones
        if not all([nombre, apellido, correo, password, confirm_password]):
            messages.error(request, "Todos los campos son obligatorios")
            return render(request, "login/registro.html")

        try:
            validate_email(correo)

        except ValidationError:
            messages.error(request, "El correo electrónico no es válido")
            return render(request, "login/registro.html")

        if password != confirm_password:

            messages.error(request, "Las contraseñas no coinciden")
            return render(request, "login/registro.html")

        if len(password) < 8:

            messages.error(request, "La contraseña debe tener al menos 8 caracteres")
            return render(request, "login/registro.html")

        
        if Controlador_usuario.usuario_existe(correo):
            messages.error(request, "Este correo electrónico ya está registrado")
            return render(request, "login/registro.html")

        try:
            # Crear el usuario
            usuario = Controlador_usuario.insertar_usuario(
                correo=correo,
                nombre=f"{nombre} {apellido}",
                contraseña=password
            )
            
            # Iniciar sesión automáticamente
            request.session["usuario_id"] = usuario.correo
            request.session["usuario_nombre"] = usuario.nombre
            
            messages.success(request, "Cuenta creada exitosamente")
            return redirect("lista_recetas")
            
        except Exception as e:
            messages.error(request, f"Error al crear la cuenta: {str(e)}")
            return render(request, "login/registro.html")

    return render(request, "login/registro.html")
