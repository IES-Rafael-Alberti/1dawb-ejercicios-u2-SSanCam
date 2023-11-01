import pytest 
from src.P2_2_8_trianguloRegresivoImpar import trianguloRegresivo

def test_triangulo_regresivo():
    assert trianguloRegresivo(3) == "1 \n3 1 \n"
    assert trianguloRegresivo(5) == "1 \n3 1 \n5 3 1 \n"

@pytest.mark.parametrize(
    "numero, expected",
        [
            (4, "1 \n3 1 \n"),
            (6, "1 \n3 1 \n5 3 1 \n")
        ]
)

def test_P2_2_8_trianguloRegresivoImpar(numero, expected):
    assert trianguloRegresivo(numero) == expected