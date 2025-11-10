def validar_receta(nombre, ingredientes, pasos):
    # Validar nombre
    if not nombre or nombre.strip() == "":
        return False

    # Validar pasos
    if not pasos or pasos.strip() == "":
        return False

    # Validar ingredientes
    if not isinstance(ingredientes, list) or len(ingredientes) == 0:
        return False

    # Validar que cada ingrediente sea válido
    for ing in ingredientes:
        if not ing or str(ing).strip() == "":
            return False

    return True

