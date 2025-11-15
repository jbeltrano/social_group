def validar_receta(nombre, ingredientes, pasos):
    """
    Valida los datos de una receta antes de guardarla.

    Parámetros:
        receta (Receta): Objeto Receta a validar

    Retorna:
        bool: True si todos los datos son válidos, False en caso contrario.
    """

    # Validar nombre
    if not validar_campos([nombre, ingredientes, pasos]):
        return False

    # Validar que no haya más de dos saltos de línea consecutivos
    if not validar_saltos_linea(ingredientes) or not validar_saltos_linea(pasos):
        return False

    ingredientes = convertir_a_lista(ingredientes)
    pasos = convertir_a_lista(pasos)


    return True


def validar_saltos_linea(texto):

    if not isinstance(texto, str):
        return False

    if '\n\n' in texto:
        return False

    return True


def convertir_a_lista(texto):
    if isinstance(texto, str):
        lista = [item.strip() for item in texto.split("\n") if item.strip()]
        return lista
    return texto


def validar_campos(campos):
    """
    Valida que todos los campos en la lista no estén vacíos o sean None.

    Parámetros:
        campos (list): Lista de campos a validar.

    Retorna:
        bool: True si todos los campos son válidos, False en caso contrario.
    """
    for campo in campos:
        if campo is None or str(campo).strip() == "":
            return False
    return True
