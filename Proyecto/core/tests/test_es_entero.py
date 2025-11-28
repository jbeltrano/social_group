import pytest
from core.controllers.Controlador_validar_tiempo import es_entero

@pytest.mark.parametrize(
    "valor, esperado",
    [
        ("10", True),       
        ("0", True),        
        ("-5", True),       
        ("3.5", False),     
        ("abc", False),     
        ("", False),       
        (None, False),      
    ]
)
def test_es_entero(valor, esperado):
    assert es_entero(valor) == esperado