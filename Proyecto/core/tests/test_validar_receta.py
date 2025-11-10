import pytest
from core.controllers.Controlador_recetas import validar_receta

@pytest.mark.parametrize(
    "nombre, ingredientes, pasos, resultado",
    [
        ("Torta de chocolate", ["harina", "huevos", "cacao"], "Mezclar y hornear", True),
        ("", ["harina", "huevos"], "Falta nombre", False),
        ("Galletas", [], "No hay ingredientes", False),
        ("Pizza", ["masa", "queso"], "", False),
        (" ", ["tomate", "cebolla"], "pasos válidos", False),
        ("Ensalada", ["lechuga", "", "tomate"], "Cortar y mezclar", False),
    ]
)
def test_validar_receta(nombre, ingredientes, pasos, resultado):
    assert validar_receta(nombre, ingredientes, pasos) == resultado
