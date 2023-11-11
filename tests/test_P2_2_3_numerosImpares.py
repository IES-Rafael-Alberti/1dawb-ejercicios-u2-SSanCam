import pytest 
from src.P2_2_3_numerosImpares import comparaNumero

def test_numero_impar():
    assert comparaNumero(6) == "Éste número es par."
    assert comparaNumero(9) == "Éste número es impar."
    
@pytest.mark.parametrize(
    "numero, expected",
    [
        (2, "Éste número es par."),
        (3, "Éste número es impar.")
    ]
)

def test_P2_2_3_numerosImpares(numero, expected):
    assert comparaNumero(numero) == expected