import pytest
from core.controllers.Controlador_validar_tiempo import validar_tiempo

@pytest.mark.parametrize(
    "cadena, esperado",
    [
        ("01:20:30", False),   
        ("10:59", False),      
        ("abc:def", False),    
        (":30:20", False),     
        ("1::20", False),      
    ]
)
def test_validar_tiempo_formato(cadena, esperado):
    
    partes = cadena.split(":")
    if len(partes) == 2:
        h, m = partes
    elif len(partes) == 3:
        h, m, _ = partes
    else:
        h, m = cadena, ""

    assert validar_tiempo(h, m) == esperado