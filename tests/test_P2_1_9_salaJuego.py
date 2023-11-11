import pytest 
from src.P2_1_9_salaJuego import precioEntrada

@pytest.mark.parametrize(
    "edad, expected",
    [
        (2, "0€"),
        (10, "5€"),
        (30, "10€")
    ]
)

def test_P2_1_9_salaJuego(edad, expected):
    assert precioEntrada(edad) == expected
    
def test_precio_entrada ():
    assert precioEntrada(2) == "0€"
    assert precioEntrada(15) == "5€"
    assert precioEntrada(25) == "10€"