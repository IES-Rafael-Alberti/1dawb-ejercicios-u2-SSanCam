import pytest 
from src.P2_2_6_trianguloAsteriscos import triangulo


def test_triangulo():
    assert triangulo(4) == "*\n**\n***\n****\n"
    assert triangulo(6) == "*\n**\n***\n****\n*****\n******\n"
@pytest.mark.parametrize(
    "niveles, expected",
    [
        (3, "*\n**\n***\n"),
        (5, "*\n**\n***\n****\n*****\n"),
        (1, "*\n")
    ]
)

def test_P2_2_6_trianguloAsteriscos(niveles, expected):
    assert triangulo(niveles) == expected