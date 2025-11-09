from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password

def validar_correo(correo):
    try:
        validate_email(correo)
        return True
    except ValidationError:
        return False


def validar_obligatoriedad(campos):
    return all(campo.strip() for campo in campos)


def validar_contraseña(contraseña_ingresada, contraseña_db):
    return check_password(contraseña_ingresada, contraseña_db)


def validar_longitud_contraseña(contraseña, longitud_minima=8):
    return len(contraseña) >= longitud_minima
