def validar_comentario(comentario):
    if not comentario:
        return False

    comentario_limpio = comentario.strip()

    # No espacios vacíos
    if comentario_limpio == "":
        return False

    # Debe tener al menos 5 caracteres
    if len(comentario_limpio) < 5:
        return False

    return True
