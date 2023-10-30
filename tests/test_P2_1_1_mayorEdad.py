import pytest
from src.P2_1_1_mayorEdad import edad

@pytest.mark.parametrize(
    "anios, expected",
    [
      (18, "Eres mayor de edad."),
      (20, "Eres mayor de edad."),
      (16, "Eres menor de edad."),
      (200, "Relája, Nosferatus.")
    ]
  )

def test_mayorEdad (anios, expected):
  assert edad(anios) == expected