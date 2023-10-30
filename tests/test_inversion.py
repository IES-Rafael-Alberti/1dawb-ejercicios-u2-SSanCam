import pytest 
from src.P2_2_EjerciciosIterativosSaltos.inversion import capitalObtenido

@pytest.mark.parametrize(
    "cantInvertir, interes, numTiempo, expected",
    [
        (200, 15, 4, "349.80€"),
        (1500, 20, 5, "3732.48€")
    ]
)

def test_inversion(cantInvertir, interes, numTiempo, expected):
    assert capitalObtenido(cantInvertir, interes, numTiempo) == expected