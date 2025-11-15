def validar_tiempo(horas, minutos):

    if not validar_campos([horas, minutos]):
        return False

    if not es_entero(horas) or not es_entero(minutos):
        return False

    horas = int(horas)
    minutos = int(minutos)


    if horas < 0 and minutos < 0 or minutos > 59:
        return False

    if minutos + horas == 0:  # El tiempo total no puede ser 0
        return False

    return True


def validar_campos(campos):
    for campo in campos:
        if campo is None or str(campo).strip() == "":
            return False
    return True


def es_entero(valor):
    try:
        int(valor)
        return True
    except (ValueError, TypeError):
        return False
