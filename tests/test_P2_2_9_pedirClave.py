import pytest 
from src.P2_2_9_pedirClave import pedirClave

@pytest.mark.parametrize(
    "clave, expected",
    [
        ("AY TORTILLA", "Contraseña correcta!"),
        ("nohaytortilla", "Contraseña incorrecta.")
    ]
)
    
def test_pedirClave(clave, expected):
    assert pedirClave(clave) == expected