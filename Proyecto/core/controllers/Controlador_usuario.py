from django.contrib.auth.hashers import make_password
from core.models.Usuario import Usuario

def obtener_todos_usuarios():
    return Usuario.objects.all()

def obtener_usuario(correo):
    return Usuario.objects.get(correo=correo)

def usuario_existe(correo):
    return Usuario.objects.filter(correo=correo).exists()

def insertar_usuario(correo, nombre, contraseña):

    contraseña = make_password(contraseña)
    nombre = nombre.strip().title()

    return Usuario.objects.create(
        nombre=nombre,
        correo=correo,
        contraseña=contraseña
    )


def actualizar_usuario(correo, nombre=None, contraseña=None):

    usuario = obtener_usuario(correo)

    if not usuario:
        return None

    if nombre is not None:
        usuario.nombre = nombre

    if contraseña is not None:
        usuario.contraseña = make_password(contraseña)

    usuario.save()
    return usuario


def eliminar_usuario(correo):
    return Usuario.objects.filter(correo=correo).delete()
