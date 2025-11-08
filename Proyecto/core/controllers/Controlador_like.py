from core.models.Like import Like
from core.models.Receta import Receta
from core.models.Usuario import Usuario

def insertar_like(usuario_correo, receta_id):
    usuario = Usuario.objects.get(correo=usuario_correo)
    receta = Receta.objects.get(id=receta_id)
    return Like.objects.create(usuario=usuario, receta=receta
                               )

def eliminar_like(usuario_correo, receta_id):
    return Like.objects.filter(usuario__correo=usuario_correo, receta__id=receta_id).delete()

def obtener_recetas_like_por_usuario(usuario_correo):
    return Receta.objects.filter(
        like__usuario__correo=usuario_correo
    ).order_by('-calificacion', '-creacion')

def es_like(usuario_correo, receta_id):
    return Like.objects.filter(usuario__correo=usuario_correo, receta__id=receta_id).exists()
