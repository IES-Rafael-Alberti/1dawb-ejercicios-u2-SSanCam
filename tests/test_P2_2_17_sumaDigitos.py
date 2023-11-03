import pytest 
from src.P2_2_17_sumaDigitos import sumaNum 

@pytest.mark.parametrize(
    "numero, expected", 
    [
        (1483, 16),
        (23,5),
        (123,6)
    ]
    
)

def test_suma_digitos(numero, expected):
    assert sumaNum(numero) == expected