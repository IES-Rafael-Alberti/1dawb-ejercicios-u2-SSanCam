import pytest
from src.P2_1_3_divisiones import division

@pytest.mark.parametrize(
    "num1, num2, expected",
    [
        (10, 5, "El resultado de dividir 10/5 es: 2.00"),
        (8, 34, "El resultado de dividir 8/34 es: 0.24"),
        (5, 0,  "ERROR.\n No puede dividirse entre 0.")
    ]
)

def test_P2_1_3_divisiones(num1, num2, expected):
    assert division(num1, num2) == expected