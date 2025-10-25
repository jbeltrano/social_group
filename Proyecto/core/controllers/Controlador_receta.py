from core.models.Receta import Receta
from .Controlador_usuario import obtener_usuario
from django.db.models import Q
from PIL import Image
import io

def obtener_recetas():
    return Receta.objects.all().order_by('-calificacion', '-creacion')

def obtener_receta(receta_id):
    return Receta.objects.get(id=receta_id)


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

def insertar_receta(nombre, imagen_file, descripcion, ingredientes, pasos, tiempo, porcion, calificacion, usuario_correo):
    """
    Inserta una nueva receta con una imagen
    :param imagen_file: Archivo de imagen (del request.FILES)
    """
    usuario = obtener_usuario(usuario_correo)

    if not usuario:
        return None
    
    # Procesar la imagen si se proporciona una
    imagen_binaria = None
    if imagen_file:
        imagen_binaria = procesar_imagen(imagen_file)
        
    return Receta.objects.create(
        nombre=nombre,
        imagen=imagen_binaria,
        descripcion=descripcion,
        ingredientes=ingredientes,
        pasos=pasos,
        tiempo=tiempo,
        porcion=porcion,
        calificacion=calificacion,
        usuario=usuario
    )

def insertar_receta(nombre, imagen, descripcion, ingredientes, pasos, tiempo, porcion, usuario_id):
    
    usuario = obtener_usuario(usuario_id)

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
        usuario=usuario
    )

def actualizar_receta(receta, nombre=None, imagen_file=None, descripcion=None, ingredientes=None, pasos=None, tiempo=None, porcion=None):
    
    if not receta:
        return None
    
    if nombre is not None:
        receta.nombre = nombre

    if imagen_file is not None:
        receta.imagen = procesar_imagen(imagen_file)

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

    receta.save()
    return receta


def eliminar_receta(receta_id):
    return Receta.objects.filter(id=receta_id).delete()


def obtener_recetas_por_tiempo(recetas, hora, minuto):
    
    
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
        
        return recetas
        
    except (ValueError, TypeError):
        return recetas

def buscar_recetas(recetas, query):
    """
    Busca recetas que coincidan con el término de búsqueda en nombre, ingredientes o porción
    :param recetas: QuerySet de recetas a filtrar
    :param query: Término de búsqueda
    :return: QuerySet filtrado de recetas
    """
        
    if not query:
        return recetas
        
    return recetas.filter(
        Q(nombre__icontains=query) |
        Q(ingredientes__icontains=query) |
        Q(porcion__icontains=query)
    )