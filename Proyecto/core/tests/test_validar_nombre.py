import pytest
from core.controllers.Controlador_validar_nombre import validar_nombre

@pytest.mark.parametrize(
    "nombre, valido",
    [
        ("Tortilla de Tortilla de Tortilla", True),
        ("", False),
        ("   ", False),
        ("                     ", False),
        ("a", True),
        ("1", True),
    ]
)
def test_validar_nombre(nombre, valido):
    assert validar_nombre(nombre) == valido