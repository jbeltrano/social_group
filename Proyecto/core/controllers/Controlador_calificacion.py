from core.models.Calificacion import Calificacion
from .Controlador_usuario import obtener_usuario
from .Controlador_receta import obtener_receta

def obtener_calificaciones():
    return Calificacion.objects.all().order_by('puntaje')

def obtener_calificaciones_por_receta(receta_id):
    return Calificacion.objects.filter(receta_id=receta_id).order_by('puntaje')

def obtener_calificacion(receta_id, usuario_correo):
    return Calificacion.objects.filter(receta_id=receta_id, usuario_correo=usuario_correo).first()


def insertar_calificacion(receta_id, usuario_correo, puntaje, comentario=None):

    receta = obtener_receta(receta_id)
    usuario = obtener_usuario(usuario_correo)

    if not receta or not usuario:
        return None

    return Calificacion.objects.create(
        receta=receta,
        usuario=usuario,
        puntaje=puntaje,
        comentario=comentario
    )


def actualizar_calificacion(receta_id, usuario_correo, puntaje=None, comentario=None):

    calificacion = obtener_calificacion(receta_id, usuario_correo)

    if not calificacion:
        return None

    if puntaje is not None:
        calificacion.puntaje = puntaje

    if comentario is not None:
        calificacion.comentario = comentario

    calificacion.save()
    return calificacion


def eliminar_calificacion(receta_id, usuario_correo):
    return Calificacion.objects.filter(receta_id=receta_id, usuario_correo=usuario_correo).delete()
