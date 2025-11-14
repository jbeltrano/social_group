import pytest
from core.controllers.Controlador_validar_descripcion import validar_descripcion

@pytest.mark.parametrize(
    "descripcion, valido",
    [
        ("Una receta corta para un desayuno express.", True),
        ("", False),
        ("   ", False),
        ("                     ", False),
        ("a", True),
        ("1", True),
    ]
)
def test_validar_descripcion(descripcion, valido):
    assert validar_descripcion(descripcion) == valido