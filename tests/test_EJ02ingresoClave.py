import pytest
from test.ingresoClave import contrasenia

@pytest.mark.parametrize(
    "cadena, expected",
    [
        ("aytortilla", "Contraseña correcta!"),
        ("ayTORTILLA", "Contraseña correcta!")
    ]
)

def test_ingresoClave(cadena, expected):
    assert contrasenia(cadena) == expected