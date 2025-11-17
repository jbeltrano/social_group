import pytest
from core.controllers.Controlador_validar_tiempo import validar_campos

@pytest.mark.parametrize(
    "campos, resultado",
    [
        (["1", "2"], True),
        (["", "2"], False),
        ([" ", "3"], False),
        ([None, "3"], False),
        (["0", "0"], True),
    ]
)
def test_validar_campos(campos, resultado):
    assert validar_campos(campos) == resultado