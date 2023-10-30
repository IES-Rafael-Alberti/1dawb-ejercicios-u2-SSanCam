import pytest
from src.P2_1_2_cadenaContrasenia import iniciarSesion

@pytest.mark.parametrize(
    "cadena, expected",
    [
        ("AYTORTILLA", "Contraseña correcta!"),
        ("AYtortilla", "Contraseña correcta!"),
        ("ayTORTILLA", "Contraseña correcta!"),
        ("noHayTortilla", "Contraseña incorrecta."),
        ("tortillasosa", "Contraseña incorrecta."),
    ]
)

def test_P2_1_2_cadenaContrasenia(cadena, expected):
    assert iniciarSesion(cadena) == expected
