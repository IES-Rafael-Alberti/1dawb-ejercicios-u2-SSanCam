import pytest 
from src.P2_1_6_asignacionGrupo import grupo 

@pytest.mark.parametrize(
    "nombre, sexo, expected",
    [
        ("zoe", "M", "Perteneces al grupo A"),
        ("antonio", "h", "Perteneces al grupo A"),
        ("ana", "m", "Perteneces al grupo B"),
        ("PACO", "H", "Perteneces al grupo B")
    ]
)

def test_P2_1_6_asignacionGrupo(nombre, sexo, expected):
    assert grupo(nombre, sexo) == expected