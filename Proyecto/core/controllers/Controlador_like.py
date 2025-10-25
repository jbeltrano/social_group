from core.models.Like import Like
from core.models.Receta import Receta
from core.models.Usuario import Usuario

def dar_like(receta_id, usuario_correo):
    """
    Da like a una receta. Si ya existe el like, lo elimina.
    Retorna True si se dio like, False si se quitó.
    """
    try:
        like = Like.objects.filter(receta_id=receta_id, usuario_correo=usuario_correo).first()
        if like:
            # Si ya existe el like, lo eliminamos
            like.delete()
            return False
        else:
            # Si no existe, lo creamos
            Like.objects.create(receta_id=receta_id, usuario_correo=usuario_correo)
            return True
    except Exception as e:
        raise e

def tiene_like(receta_id, usuario_correo):
    """
    Verifica si un usuario ya dio like a una receta
    """
    return Like.objects.filter(receta_id=receta_id, usuario_correo=usuario_correo).exists()

def contar_likes(receta_id):
    """
    Cuenta el número de likes de una receta
    """
    return Like.objects.filter(receta_id=receta_id).count()