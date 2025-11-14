def validar_descripcion(descripcion):
    if not descripcion:
        return False

    sin_descripcion = descripcion.strip()

    # No espacios vacíos
    if sin_descripcion == "":
        return False

    return True
