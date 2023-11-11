import pytest 
from src.P2_2_4_cuentaAtras import restaSeriada

def test_cuenta_atras():
    assert restaSeriada(4) == "4, 3, 2, 1, 0"
    assert restaSeriada(5) == "5, 4, 3, 2, 1, 0"
    
@pytest.mark.parametrize(
    "numero, expected",
    [
        (3, "3, 2, 1, 0"),
        (6, "6, 5, 4, 3, 2, 1, 0")
    ]
)

def test_P2_2_4_cuentaAtras(numero, expected):
    assert restaSeriada(numero) == expected