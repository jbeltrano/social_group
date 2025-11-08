import io
from PIL import Image
from django.db.models import Q
from core.models.Receta import Receta
from .Controlador_usuario import obtener_usuario
from .Controlador_validar_receta import validar_receta

def obtener_receta_vacia():
    receta = Receta()
    return receta

def obtener_recetas():
    return Receta.objects.all().order_by('-calificacion_avg', '-creacion')


def obtener_receta(receta_id):
    if not Receta.objects.filter(id=receta_id).exists():
        return None
    return Receta.objects.get(id=receta_id)


def obtener_recetas_por_usuario(usuario_correo):
    return Receta.objects.filter(usuario__correo=usuario_correo).order_by('-creacion')


def procesar_imagen(imagen_file, max_size=(800, 800)):
    """
    Procesa una imagen para optimizarla y convertirla a formato binario
    :param imagen_file: Archivo de imagen (del request.FILES)
    :param max_size: Tamaño máximo de la imagen (ancho, alto)
    :return: Datos binarios de la imagen
    """
    # Abrir la imagen usando Pillow
    image = Image.open(imagen_file)

    # Convertir a RGB si es necesario
    if image.mode in ('RGBA', 'P'):
        image = image.convert('RGB')

    # Redimensionar si es necesario, manteniendo la proporción
    image.thumbnail(max_size, Image.Resampling.LANCZOS)

    # Guardar la imagen en un buffer de memoria
    buffer = io.BytesIO()
    image.save(buffer, format='JPEG', quality=85, optimize=True)

    # Obtener los datos binarios
    return buffer.getvalue()


def insertar_receta(
        receta,
        imagen_file,
        hora,
        minuto,
        usuario_correo
    ):

    usuario = obtener_usuario(usuario_correo)

    tiempo = convertir_hora_minuto_a_tiempo(hora, minuto)

    if not usuario:
        return None

    # Procesar la imagen si se proporciona una
    if imagen_file:
        receta.imagen = procesar_imagen(imagen_file)

    receta.usuario = usuario
    receta.tiempo = tiempo
    if not validar_receta(receta):
        return None

    receta.save()
    return receta



def actualizar_receta(receta, imagen_file=None, hora=None, minuto=None):

    if not receta:
        return None

    if imagen_file is not None:
        receta.imagen = procesar_imagen(imagen_file)

    if hora is not None or minuto is not None:
        receta.tiempo = convertir_hora_minuto_a_tiempo(hora, minuto)

    receta.save()
    return receta


def eliminar_receta(receta_id):
    return Receta.objects.filter(id=receta_id).delete()


def obtener_recetas_por_tiempo(recetas, hora, minuto, usuario_id=None):

    tiempo_total_minutos = 0
    try:
        if hora and hora.isdigit():
            tiempo_total_minutos += int(hora) * 60

        if minuto and minuto.isdigit():
            tiempo_total_minutos += int(minuto)

        if tiempo_total_minutos > 0:
            horas = tiempo_total_minutos // 60
            minutos = tiempo_total_minutos % 60
            tiempo_objetivo = f"{horas:02d}:{minutos:02d}:00"

            return recetas.filter(tiempo__lte=tiempo_objetivo)

        if usuario_id:
            return recetas.filter(usuario__correo=usuario_id)

        return recetas

    except (ValueError, TypeError):
        return recetas

def convertir_hora_minuto_a_tiempo(hora, minuto):
    """
    Convierte horas y minutos a un objeto de tiempo en formato HH:MM:SS
    :param hora: Número de horas
    :param minuto: Número de minutos
    :return: String en formato HH:MM:SS
    """
    try:
        horas = int(hora) if hora and str(hora).isdigit() else 0
        minutos = int(minuto) if minuto and str(minuto).isdigit() else 0

        total_minutos = horas * 60 + minutos
        horas_finales = total_minutos // 60
        minutos_finales = total_minutos % 60

        return f"{horas_finales:02d}:{minutos_finales:02d}:00"

    except (ValueError, TypeError):
        return "00:00:00"


def buscar_recetas(recetas, query):
    """
    Busca recetas que coincidan con el término de búsqueda en nombre, ingredientes o porción
    :param recetas: QuerySet de recetas a filtrar
    :param query: Término de búsqueda
    :return: QuerySet filtrado de recetas
    """
    return recetas.filter(
        Q(nombre__icontains=query) |
        Q(ingredientes__icontains=query) |
        Q(porcion__icontains=query)
    )


def buscar_recetas_usuario(recetas, query, usuario_id):
    """
    Busca recetas que coincidan con el término de búsqueda en nombre, ingredientes o porción
    :param recetas: QuerySet de recetas a filtrar
    :param query: Término de búsqueda
    :return: QuerySet filtrado de recetas
    """

    return recetas.filter(
        Q(nombre__icontains=query) |
        Q(ingredientes__icontains=query) |
        Q(porcion__icontains=query)
    ).filter(usuario__correo = usuario_id)


def buscar_recetas_favoritas_usuario(recetas, query, usuario_id):
    """
    Busca recetas favoritas que coincidan con el
    término de búsqueda en nombre, ingredientes o porción
    :param recetas: QuerySet de recetas a filtrar
    :param query: Término de búsqueda
    :return: QuerySet filtrado de recetas favoritas
    """

    return recetas.filter(
        Q(nombre__icontains=query) |
        Q(ingredientes__icontains=query) |
        Q(porcion__icontains=query)
    ).filter(favoritos__usuario__correo = usuario_id)
