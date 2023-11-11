import pytest
from src.P2_2_2_todosAnios import cantidadAnios

@pytest.mark.parametrize(
    "edad, expected",
    [
      (5, "1, 2, 3, 4, 5"),
      (3, "1, 2, 3")
    ]
)

def test_P2_2_2_todosAnios(edad, expected):
    assert cantidadAnios(edad) == expected