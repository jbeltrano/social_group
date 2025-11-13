# core/controllers/Controlador_receta.py

from core.models import Receta, Usuario
from datetime import timedelta


def validar_receta(nombre, ingredientes, pasos):
    """
    Valida los datos de una receta antes de guardarla.

    Parámetros:
        receta (Receta): Objeto Receta a validar

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