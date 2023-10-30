import pytest 
from src.P2_1_1_mayorEdad import mayorEdad

@pytest.mark.parametrize(
    "anios, expected",
    [
        (20, "Eres mayor de edad."),
        (5, "Eres menor de edad."),
        (200, "Relája, Nosferatu.")
    ]
)

def test_P2_1_1_mayorEdad(anios, expected):
    assert mayorEdad(anios) == expected