import pytest
from core.controllers.Controlador_validaciones import validar_obligatoriedad
from core.controllers.Controlador_validaciones import validar_correo
from core.controllers.Controlador_validaciones import validar_longitud_contraseña
from core.controllers.Controlador_validaciones import validar_contraseña
from core.controllers.Controlador_login import verificar_registro
from django.contrib.auth.hashers import make_password

@pytest.mark.parametrize(
    "nombre, apellido, correo, contraseña, contraseña_confirmada, resultado",
    [
        ("Juan", "Beltran","juan@gmail.com","12345678","12345678", True),
        ("", "Beltran","juan@gmail.com","12345678","12345678", False),
        ("Juan", "","juan@gmail.com","12345678","12345678", False),
        ("Juan", "Beltran","","12345678","12345678", False),
        ("Juan", "Beltran","juan@gmail.com","","12345678", False),
        ("Juan", "Beltran","juan@gmail.com","12345678","", False),
        ("", "","","","", False),
        ("", "","juan@gmail.com","12345678","12345678", False),
        ("", "Beltran","","12345678","", False),
    ]
)

def test_verificar_registro_campos_obligatorios(nombre, apellido, correo, contraseña, contraseña_confirmada, resultado):
    
    assert validar_obligatoriedad([nombre, apellido, correo, contraseña, contraseña_confirmada]) == resultado


@pytest.mark.parametrize(
    "correo, resultado",
    [
        ("juan@gmail.com", True),
        ("correo_invalido", False),
        ("", False),
        ("juan@", False),
        ("juan@gmail", False),
        ("juan@gmail.c", False),
        ("juan@.com", False),
        ("juan@yahoo.es", True),
    ]
)

def test_validar_correo(correo, resultado):
    assert validar_correo(correo) == resultado

@pytest.mark.parametrize(
    "password, resultado",
    [
        ("12345678", True),
        ("asdfghjk", True),
        ("1a2s3d4f", True),
        ("laksjdfñlkaj123423asdfas", True),
        ("1234567", False),
        ("abcd123", False),
        ("123", False),
        ("abc", False),
        ("", False),
    ]
)

def test_validar_longitud_contraseña(password, resultado):
    assert validar_longitud_contraseña(password) == resultado

@pytest.mark.parametrize(
    "nombre, apellido, correo, contraseña, contraseña_confirmada, resultado",
    [
        ("Juan", "Beltran","juan@gmail.com","12345678","12345678", []),
        ("", "Beltran","juan@gmail.com","12345678","12345678", ["Todos los campos son obligatorios."]),
        ("Juan", "Beltran","juan@.com","asdfghjk","asdfghjk", ["El correo electrónico no es válido."]),
        ("Juan", "Beltran","juan@gmail.com","1234","1234", ["La contraseña debe tener al menos 8 caracteres."]),
        ("Juan", "Beltran","juan@gmail.com","1a2b345678","1a2b345678as", ["Las contraseñas no coinciden."]),
    ]
)

def test_verificar_registro(nombre, apellido, correo, contraseña, contraseña_confirmada, resultado):
    assert verificar_registro(nombre, apellido, correo, contraseña, contraseña_confirmada) == resultado


@pytest.mark.parametrize(
    "contraseña_ingresada, contraseña_db, resultado",
    [
        ("12345678",make_password("12345678"), True),
        ("password", make_password("password"), True),
        ("wrongpassword", make_password("12345678"), False),
        ("anotherwrong", make_password("password"), False),
        ("", make_password("password"), False),
        ("12345678", "", False),
        ("12345678", "12345678", False),
    ]
)

def test_validar_contraseña(contraseña_ingresada, contraseña_db, resultado):
    assert validar_contraseña(contraseña_ingresada, contraseña_db) == resultado