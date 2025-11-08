from core.models.Favorito import Favorito
from core.models.Receta import Receta
from core.models.Usuario import Usuario

def insertar_favorito(usuario_correo, receta_id):
    usuario = Usuario.objects.get(correo=usuario_correo)
    receta = Receta.objects.get(id=receta_id)
    return Favorito.objects.create(usuario=usuario, receta=receta)

def eliminar_favorito(usuario_correo, receta_id):
    return Favorito.objects.filter(usuario__correo=usuario_correo, receta__id=receta_id).delete()

def obtener_recetas_favoritas_por_usuario(usuario_correo):
    return Receta.objects.filter(
        favorito__usuario__correo=usuario_correo
    ).order_by('-calificacion_avg', '-creacion')

def es_favorito(usuario_correo, receta_id):
    return Favorito.objects.filter(usuario__correo=usuario_correo, receta__id=receta_id).exists()
