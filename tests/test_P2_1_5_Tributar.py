import pytest 
from src.P2_1_5_Tributar import aptoTributar

@pytest.mark.parametrize(
    "edad, ingresos, expected",
    [
        (17, 1000, "Puedes tributar."),
        (20, 1002.23, "Puedes tributar."),
        (16, 1000, "No cumples los requisitos necesarios para tributar."),
        (15, 1000000.00, "No cumples los requisitos necesarios para tributar.")
    ]
)

def test_P2_1_5_Tributar(edad, ingresos, expected):
    assert aptoTributar(edad, ingresos) == expected