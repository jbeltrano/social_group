def validar_tiempo(horas, minutos):
    if horas is None or minutos is None:
        return False

    # Si son strings, intentar limpiarlos y convertirlos
    if isinstance(horas, str):
        horas = horas.strip()
        if horas == "":
            return False
        try:
            horas = int(horas)
        except ValueError:
            return False

    if isinstance(minutos, str):
        minutos = minutos.strip()
        if minutos == "":
            return False
        try:
            minutos = int(minutos)
        except ValueError:
            return False

    if not isinstance(horas, int) or not isinstance(minutos, int):
        return False

    if horas < 0:  # No existe el tiempo negativo
        return False

    if minutos < 0:  # No existe el tiempo negativo
        return False

    if minutos > 59:  # 60 minutos son una hora
        return False

    if minutos + horas == 0:  # El tiempo total no puede ser 0
        return False

    return True
