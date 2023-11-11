import pytest 
from src.P2_2_1_repeticionPalabras import repeticion 

@pytest.mark.parametrize(
    "palabra, expected",
    [
        ("palabra", "palabra, palabra, palabra, palabra, palabra, palabra, palabra, palabra, palabra, palabra")
    ]
)
def test_P2_2_1_repeticionPalabras(palabra, expected):
    assert repeticion(palabra) == expected

def test_repeticion_palabra():
    assert repeticion("palabra") == "palabra, palabra, palabra, palabra, palabra, palabra, palabra, palabra, palabra, palabra"