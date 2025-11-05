from core.models.Favorito import Favorito
from core.models.Receta import Receta

def insertar_favorito(usuario, receta):
    favorito = Favorito(usuario=usuario, receta=receta)
    favorito.save()
    return favorito

def eliminar_favorito(usuario_correo, receta_id):
    return Favorito.objects.filter(usuario__correo=usuario_correo, receta__id=receta_id).delete()

def obtener_recetas_favoritas_por_usuario(usuario_correo):
    return Receta.objects.filter(favorito__usuario__correo=usuario_correo).order_by('-calificacion', '-creacion')