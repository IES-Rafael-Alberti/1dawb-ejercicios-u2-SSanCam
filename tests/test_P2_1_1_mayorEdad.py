import pytest
from src.P2_1_1_mayorEdad import pytest

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
  assert test_mayorEdad(anios) == expected