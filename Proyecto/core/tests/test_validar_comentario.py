import pytest
from core.controllers.Controlador_comentarios import validar_comentario

@pytest.mark.parametrize(
    "comentario, resultado",
    [
        ("Me encantó esta receta!", True),
        ("", False),
        ("   ", False),
        ("mal", False),   # demasiado corto
        ("Excelente", True),
        ("12345", True),  # exactamente el mínimo permitido
    ]
)
def test_validar_comentario(comentario, resultado):
    assert validar_comentario(comentario) == resultado
