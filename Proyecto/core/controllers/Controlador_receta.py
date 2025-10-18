from core.models.Receta import Receta
from .Controlador_usuario import obtener_usuario

def crear_receta(nombre, imagen, descripcion, ingredientes, pasos, tiempo, porcion, calificacion, usuario_correo):
    usuario = obtener_usuario(usuario_correo).first()
    if usuario:
        return Receta.objects.create(
            nombre=nombre,
            imagen=imagen,
            descripcion=descripcion,
            ingredientes=ingredientes,
            pasos=pasos,
            tiempo=tiempo,
            porcion=porcion,
            calificacion=calificacion,
            usuario_correo=usuario
        )
    return None

def obtener_recetas():
    return Receta.objects.all()