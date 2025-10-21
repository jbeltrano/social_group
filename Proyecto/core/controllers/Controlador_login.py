from django.contrib.auth.hashers import check_password
from .Controlador_usuario import obtener_usuario
from core.models.Usuario import Usuario

def verificar_login(correo, contraseña):
    try:
        usuario = obtener_usuario(correo=correo)
        if check_password(contraseña, usuario.contraseña):
            return usuario
        else:
            return None
    except Usuario.DoesNotExist:
        return None
