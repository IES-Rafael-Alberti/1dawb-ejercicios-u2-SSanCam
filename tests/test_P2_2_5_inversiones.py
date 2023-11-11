import pytest 
from src.P2_2_5_inversiones import capitalObtenido

def test_capital_obtenido():
    assert capitalObtenido(1000, 10, 1) == "1100.00€"
    assert capitalObtenido(2500, 20, 1) == "3000.00€"
    
@pytest.mark.parametrize(
    "inversion, interes, anios, expected",
    [
        (5000, 35, 2, "9112.50€"),
        (25500, 35, 3, "62739.56€")
    ]
)

def test_P2_2_5_inversiones(inversion, interes, anios, expected):
    assert capitalObtenido(inversion, interes, anios) == expected