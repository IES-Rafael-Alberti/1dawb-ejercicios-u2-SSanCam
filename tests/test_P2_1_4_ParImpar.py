import pytest
from src.P2_1_4_ParImpar import pares

@pytest.mark.parametrize(
    "numero, expected",
    [
        (8, "El número es par."),
        (9, "El número es impar.")
    ]
)

def test_P2_1_4_ParImpar(numero, expected):
    assert pares(numero) == expected