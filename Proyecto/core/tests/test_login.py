import pytest
from core.controllers.Controlador_validaciones import validar_obligatoriedad
from core.controllers.Controlador_validaciones import validar_correo
from core.controllers.Controlador_validaciones import validar_longitud_contraseña
from core.controllers.Controlador_login import verificar_registro

@pytest.mark.parametrize(
    "nombre, apellido, correo, contraseña, contraseña_confirmada, resultado",
    [
        ("Todos", "los","campos","tienen","valor", True),
        ("", "falta","un","unico","campo", False),
        ("falta", "","un","campo","en otro lugar", False),
        ("falta", "un","","campo","en otro lugar", False),
        ("falta", "un","campo","","en otro lugar", False),
        ("falta", "un","campo","en otro lugar","", False),
        ("", "","","","", False),
        ("", "","falta","mas de un","campo", False),
        ("", "falta mas de un","","campo","", False),
        (" ", "falta mas de un"," ","campo","", False),
    ]
)

def test_verificar_registro_campos_obligatorios(nombre, apellido, correo, contraseña, contraseña_confirmada, resultado):
    assert validar_obligatoriedad([nombre, apellido, correo, contraseña, contraseña_confirmada]) == resultado


@pytest.mark.parametrize(
    "correo, resultado",
    [
        ("correo@valido.com", True),
        ("correo_invalido", False),
        ("", False),
        ("sin_dominio_ni_extencion@", False),
        ("sin@extencion", False),
        ("extencion@incompleta.c", False),
        ("sin_dominio@.com", False),
        ("con espacio@yahoo.es", False),
    ]
)

def test_validar_correo(correo, resultado):
    assert validar_correo(correo) == resultado

@pytest.mark.parametrize(
    "password, resultado",
    [
        ("es suficientemente larga", True),
        ("escorta", False),
        ("8 exacto", True),
    ]
)

def test_validar_longitud_contraseña(password, resultado):
    assert validar_longitud_contraseña(password) == resultado

@pytest.mark.parametrize(
    "nombre, apellido, correo, contraseña, contraseña_confirmada, resultado",
    [
        ("todos", "los","camopos@estan.com","completos","completos", []),
        ("", "falta","algun@campo.com","incompleto","incompleto", ["Todos los campos son obligatorios."]),
        ("El", "correo","no@.com","es valido","es valido", ["El correo electrónico no es válido."]),
        ("La", "contraseña","es@gmail.com","corta","corta", ["La contraseña debe tener al menos 8 caracteres."]),
        ("las", "contraseñas","son@gmail.com","igualiticas","no son igualiticas", ["Las contraseñas no coinciden."]),
    ]
)

def test_verificar_registro(nombre, apellido, correo, contraseña, contraseña_confirmada, resultado):
    assert verificar_registro(nombre, apellido, correo, contraseña, contraseña_confirmada) == resultado
