from core.models.Receta import Receta
from .Controlador_usuario import obtener_usuario

def obtener_recetas():
    return Receta.objects.all()

def obtener_receta(receta_id):
    return Receta.objects.filter(id=receta_id).first()


def insertar_receta(nombre, imagen, descripcion, ingredientes, pasos, tiempo, porcion, calificacion, usuario_correo):

    usuario = obtener_usuario(usuario_correo)

    if not usuario:
        return None
        
    return Receta.objects.create(
        nombre=nombre,
        imagen=imagen,
        descripcion=descripcion,
        ingredientes=ingredientes,
        pasos=pasos,
        tiempo=tiempo,
        porcion=porcion,
        calificacion=calificacion,
        usuario=usuario
    )


def actualizar_receta(receta_id, nombre=None, imagen=None, descripcion=None, ingredientes=None, pasos=None, tiempo=None, porcion=None, calificacion=None):
    
    receta = obtener_receta(receta_id)
    
    if not receta:
        return None
    
    if nombre is not None:
        receta.nombre = nombre

    if imagen is not None:
        receta.imagen = imagen

    if descripcion is not None:
        receta.descripcion = descripcion

    if ingredientes is not None:
        receta.ingredientes = ingredientes

    if pasos is not None:
        receta.pasos = pasos

    if tiempo is not None:
        receta.tiempo = tiempo

    if porcion is not None:
        receta.porcion = porcion

    if calificacion is not None:
        receta.calificacion = calificacion

    receta.save()
    return receta


def eliminar_receta(receta_id):
    return Receta.objects.filter(id=receta_id).delete()