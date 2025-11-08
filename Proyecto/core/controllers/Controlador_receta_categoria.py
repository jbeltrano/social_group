from core.models.Receta_categoria import Receta_categoria
from core.models.Receta import Receta
from . import Controlador_receta
from . import Controlador_categoria

def obtener_recetas_categorias():
    return Receta_categoria.objects.all()

def obtener_receta_categoria(categoria_id):
    return Receta_categoria.objects.filter(categoria_id=categoria_id)

def obtener_categorias_de_receta(receta_id):
    return Receta_categoria.objects.filter(
        receta_id=receta_id
    ).all().values_list('categoria_id', flat=True)

def insertar_receta_categoria(receta_id, categoria_id):

    receta = Controlador_receta.obtener_receta(receta_id)
    categoria = Controlador_categoria.obtener_categoria(categoria_id)

    if not receta or not categoria:
        return None

    return Receta_categoria.objects.create(
        receta=receta,
        categoria=categoria
    )


def eliminar_receta_categoria(receta_id, categoria_id):
    return Receta_categoria.objects.filter(
        receta_id=receta_id,
        categoria_id=categoria_id
    ).delete()

def eliminar_categorias_de_receta(receta_id):
    return Receta_categoria.objects.filter(
        receta_id=receta_id
    ).delete()

def obtener_recetas_por_categoria(categoria_id, usuario_id=None):
    """
    Obtiene todas las recetas que pertenecen a una categoría específica.
    Args:
        categoria_id: ID de la categoría
        usuario_id: (opcional) correo electrónico del usuario para filtrar las recetas por usuario
    Returns:
        QuerySet de objetos Receta que pertenecen a la categoría especificada
    """
    if usuario_id:
        return Receta.objects.filter(
            receta_categoria__categoria_id=categoria_id,
            usuario__correo=usuario_id
        ).order_by('-calificacion', '-creacion')

    return Receta.objects.filter(
        receta_categoria__categoria_id=categoria_id
        ).order_by('-calificacion', '-creacion')
