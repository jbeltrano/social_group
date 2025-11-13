# core/controllers/Controlador_receta.py

from core.models import Receta, Usuario
from datetime import timedelta


def validar_receta(nombre, ingredientes, pasos):
    """
    Valida los datos de una receta antes de guardarla.

    Parámetros:
        nombre (str): Nombre de la receta.
        ingredientes (str | list[str]): Ingredientes como texto (con saltos de línea) o lista.
        pasos (str): Pasos de preparación.

    Retorna:
        bool: True si todos los datos son válidos, False en caso contrario.
    """

    # Validar nombre
    if not nombre or nombre.strip() == "":
        return False

    # Validar pasos
    if not pasos or pasos.strip() == "":
        return False

    # Si los ingredientes vienen como string, convertirlos en lista (separar por saltos de línea)
    if isinstance(ingredientes, str):
        ingredientes = [i.strip() for i in ingredientes.split("\n") if i.strip()]

    # Validar que sea lista y no esté vacía
    if not isinstance(ingredientes, list) or len(ingredientes) == 0:
        return False

    # Validar cada ingrediente
    for ing in ingredientes:
        if not ing or str(ing).strip() == "":
            return False

    return True


def insertar_receta(receta, imagen_file=None, hora=0, minuto=0, usuario_correo=None):
    """
    Inserta una receta en la base de datos con validación.
    Esta versión acepta los mismos argumentos que usa tu vista 'formulario_receta'.

    Parámetros:
        receta (Receta): Objeto del modelo Receta.
        imagen_file (InMemoryUploadedFile, opcional): Imagen de la receta.
        hora (int|str): Horas del tiempo de preparación.
        minuto (int|str): Minutos del tiempo de preparación.
        usuario_correo (str): Correo del usuario que crea la receta.

    Retorna:
        Receta | None: Retorna la receta guardada si es válida, None si es inválida.
    """

    # Convertir hora y minuto a timedelta
    try:
        hora = int(hora) if hora else 0
        minuto = int(minuto) if minuto else 0
        receta.tiempo = timedelta(hours=hora, minutes=minuto)
    except ValueError:
        receta.tiempo = timedelta(minutes=0)

    # Asignar imagen si se proporcionó
    if imagen_file:
        receta.imagen = imagen_file

    # Asignar usuario si se proporcionó el correo
    if usuario_correo:
        usuario = Usuario.objects.filter(correo=usuario_correo).first()
        if usuario:
            receta.usuario = usuario

    #  Validar antes de guardar
    if not validar_receta(receta.nombre, receta.ingredientes, receta.pasos):
        print(" Receta inválida: falta nombre, ingredientes o pasos.")
        return None

    # Guardar en base de datos
    receta.save()
    return receta
