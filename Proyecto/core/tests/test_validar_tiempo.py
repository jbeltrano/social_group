import pytest
from core.controllers.Controlador_validar_tiempo import validar_tiempo

@pytest.mark.parametrize(
    "horas, minutos, valido",
    [
        ("1", "1", True),
        ("", "1", False),
        ("1", "", False),
        ("", "", False),
        ("-1", "1" ,False),
        ("1", "-1", False),
        ("-1", "-1", False),
        ("0", "0", False),
        ("99999", "59", True),
        ("0", "60", False),
        ("a", "1", False),
        ("1", "a", False),
        ("a", "a", False),
        ("0", "50", True),
    ]
)
def test_validar_tiempo(horas, minutos, valido):
    assert validar_tiempo(horas, minutos) == valido