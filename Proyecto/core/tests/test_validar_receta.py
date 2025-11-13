# tests/test_validar_receta.py

import pytest
from core.controllers.Controlador_receta import validar_receta


@pytest.mark.parametrize(
    "nombre, ingredientes, pasos, resultado",
    [
        #  Caso válido
        (
            "Torta de chocolate",
            "harina\nhuevos\ncacao en polvo",
            "Mezclar todos los ingredientes y hornear por 45 minutos.",
            True,
        ),
        #  Nombre vacío
        (
            "",
            "harina\nhuevos",
            "Falta nombre",
            False,
        ),
        #  Ingredientes vacíos
        (
            "Galletas",
            "",
            "No hay ingredientes",
            False,
        ),
        #  Pasos vacíos
        (
            "Pizza",
            "masa\nqueso\nsalsa de tomate",
            "",
            False,
        ),
        #  Nombre con solo espacios
        (
            "   ",
            "tomate\ncebolla\norégano",
            "Pasos válidos",
            False,
        ),
        #  Ingrediente vacío entre líneas
        (
            "Ensalada",
            "lechuga\n\ntomate",
            "Cortar y mezclar todos los ingredientes frescos.",
            False,
        ),
        #  Ingredientes válidos con espacios adicionales
        (
            "Pan casero",
            "  harina  \n  agua  \n  levadura  ",
            "Amasar y hornear durante 30 minutos.",
            True,
        ),
    ],
)
def test_validar_receta(nombre, ingredientes, pasos, resultado):
    """
    Prueba unitaria para validar_receta() con ingredientes como texto con saltos de línea.
    Verifica que la validación funcione correctamente para distintos casos.
    """
    assert validar_receta(nombre, ingredientes, pasos) == resultado
