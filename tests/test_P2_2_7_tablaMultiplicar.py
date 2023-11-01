import pytest 
from src.P2_2_7_tablaMultiplicar import multiplicacion

def test_multiplicacion():
    assert multiplicacion(2) == "2 x 1 = 2\n2 x 2 = 4\n2 x 3 = 6\n2 x 4 = 8\n2 x 5 = 10\n2 x 6 = 12\n2 x 7 = 14\n2 x 8 = 16\n2 x 9 = 18\n2 x 10 = 20\n"
    
@pytest.mark.parametrize(
    "numero, expected",
    [
        (4, "4 x 1 = 4\n4 x 2 = 8\n4 x 3 = 12\n4 x 4 = 16\n4 x 5 = 20\n4 x 6 = 24\n4 x 7 = 28\n4 x 8 = 32\n4 x 9 = 36\n4 x 10 = 40\n")
    ]
)

def test_P2_2_7_tablaMultiplicar(numero, expected):
    assert multiplicacion(numero) == expected