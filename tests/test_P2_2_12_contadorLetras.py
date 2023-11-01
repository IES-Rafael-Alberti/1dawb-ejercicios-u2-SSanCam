import pytest 
from src.P2_2_12_contadorLetras import contadorLetras

def test_contador_letras():
    assert contadorLetras("sara", "l") == 0
    assert contadorLetras("la zarzamora llora, llora", "R") == 4
    
@pytest.mark.parametrize(
    "frase, letra, expected",
    [
        ("Nicolas Cage", "B", 0),
        ("maravillosas peliculas", "a", 4)
    ]
)

def test_ocurrenciasLetra(frase, letra, expected):
    assert contadorLetras(frase, letra) == expected