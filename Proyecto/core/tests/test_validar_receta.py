# tests/test_validar_receta.py

import pytest
from core.controllers.Controlador_recetas import validar_receta


@pytest.mark.parametrize(
    "nombre, ingredientes, pasos, resultado",
    [
        (
            "Torta de chocolate",
            "harina\nhuevos\ncacao",
            "Mezclar y hornear",
            True,
        ),
        (
            "",
            "harina\nhuevos",
            "Falta nombre",
            False,
        ),
        (
            "Galletas",
            "",
            "No hay ingredientes",
            False,
        ),
        (
            "Pizza",
            "masa\nqueso",
            "",
            False,
        ),
        (
            " ",
            "tomate\ncebolla",
            "pasos válidos",
            False,
        ),
        (
            "Ensalada",
            "lechuga\n\ntomate",
            "Cortar y mezclar",
            False,
        ),
    ],
)
def test_validar_receta(nombre, ingredientes, pasos, resultado):
    """
    Prueba unitaria para validar_receta() con ingredientes como texto con saltos de línea.
    """
    resultado_obtenido = validar_receta(nombre, ingredientes, pasos)
    assert resultado_obtenido == resultado

