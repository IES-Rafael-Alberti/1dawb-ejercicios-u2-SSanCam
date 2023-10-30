import pytest
from src.P2_1_2_ingresoClave import contrasenia

@pytest.mark.parametrize(
    "cadena, expected",
    [
        ("AYtortilla", "Contraseña correcta."),
        ("ayTORTILLA", "Contraseña correcta."),
        ("nohaytortilla", "Contraseña incorrecta.")
    ]
)
def test_contrasenia(cadena, expected):
    assert contrasenia(cadena) == expected