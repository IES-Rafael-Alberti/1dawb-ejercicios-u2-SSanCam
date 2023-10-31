import pytest 
from src.P2_1_6_asignacionGrupo import grupo 

"""@pytest.mark.parametrize(
    "nombre, sexo, expected",
    [
        ("zoe", "M", "Perteneces al grupo A"),
        ("antonio", "h", "Perteneces al grupo A"),
        ("ana", "m", "Perteneces al grupo B"),
        ("PACO", "H", "Perteneces al grupo B")
    ]
)

def test_P2_1_6_asignacionGrupo(nombre, sexo, expected):
    assert grupo(nombre, sexo) == expected"""
    
    
def test_asignacion_grupo_A():
    assert grupo("zoe", "M") == "Perteneces al grupo A"
    assert grupo("antonio", "h") == "Perteneces al grupo A"

def test_asignacion_grupo_B():
    assert grupo("ana", "m") == "Perteneces al grupo B"
    assert grupo("PACO", "H") == "Perteneces al grupo B"