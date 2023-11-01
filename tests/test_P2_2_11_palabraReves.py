import pytest 
from src.P2_2_11_palabraReves import revesPalabra

def test_palabra_reves():
    assert revesPalabra("sara") == "aras"
    assert revesPalabra("sara camilleri") == "irellimac aras"
    
@pytest.mark.parametrize(
    "palabra, expected",
    [
        ("espetaculá", "álucatepse")
    ]
)

def test_reves_palabra(palabra, expected):
    assert revesPalabra(palabra) == expected 