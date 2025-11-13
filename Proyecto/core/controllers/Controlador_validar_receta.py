# core/controllers/Controlador_recetas.py

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


def insertar_receta(receta):
    """
    Inserta la receta en la base de datos solo si es válida.
    
    Parámetros:
        receta (Receta): Objeto modelo de Django.
    
    Retorna:
        bool: True si se guardó, False si es inválida.
    """

    # Validar los campos de la receta usando la función validar_receta
    if not validar_receta(
        receta.nombre,
        receta.ingredientes,  # puede ser string con saltos de línea o lista
        receta.pasos
    ):
        # Aquí puedes agregar un mensaje de error o logging si quieres
        print("Receta inválida: nombre, ingredientes o pasos incorrectos")
        return False

    # Guardar en la base de datos
    receta.save()
    return True
