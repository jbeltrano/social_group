from core.models.Usuario import Usuario
from django.contrib.auth.hashers import make_password

def crear_usuario(correo, nombre, contraseña):

    contraseña = make_password(contraseña)
    
    return Usuario.objects.create(
        nombre=nombre,
        correo=correo,
        password=contraseña
    )

def obtener_usuario(correo):
    return Usuario.objects.filter(correo=correo)

def actualizar_usuario(correo, nombre, contraseña):
    return Usuario.objects.update(nombre=nombre, password=contraseña).filter(correo=correo)

def eliminar_usuario(correo):
    return Usuario.objects.filter(correo=correo).delete()

def obtener_todos_usuarios():
    return Usuario.objects.all()