def validar_nombre(nombre):
    if not nombre:
        return False

    sin_nombre = nombre.strip()

    if sin_nombre == "":
        return False

    return True