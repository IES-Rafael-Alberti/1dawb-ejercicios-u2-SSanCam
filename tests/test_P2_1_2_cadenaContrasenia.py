import pytest
from src.P2_1_2_cadenaContrasenia import iniciarSesion
from src.P2_2_9_pedirClave import comprobarClave

@pytest.mark.parametrize(
    "cadena, expected",
    [
        ("AYTORTILLA", "Contraseña correcta!"),
        ("AY tortilla", "Contraseña correcta!"),
        ("ayTORTILLA", "Contraseña correcta!"),
        ("noHayTortilla", "Contraseña incorrecta."),
        ("tortillasosa", "Contraseña incorrecta."),
    ]
)

def test_P2_1_2_cadenaContrasenia(cadena, expected):
    assert iniciarSesion(cadena) == expected
    
####___test re-ingreso contraseña___#### 
## P2_2_9_pedirClave() ##
    
def test_comprobar_clave():
    assert comprobarClave("aytortilla") == "Contraseña correcta!"
    assert comprobarClave("NOhaytortilla") == "Contraseña incorrecta."

@pytest.mark.parametrize(
    "clave, expected",
    [
        ("ay TOR tilla", "Contraseña correcta!"),
        ("hayTHORtilla", "Contraseña incorrecta.")
    ]
)
def test_comprobar_clave(clave, expected):
    assert comprobarClave(clave) == expected