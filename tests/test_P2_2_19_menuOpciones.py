import pytest 
from src.P2_2_19_menuOpciones import menu_op

@pytest.mark.parametrize(
    "opcion, expected",
    [
        (1, "***INICIANDO PROGRAMA***"),
        (2, "***IMPRIMIENDO LISTADO***"),
        (3, "**SALIENDO DEL PROGRAMA**"),
        (7, "Debes elegir entre las opciones 1, 2 y 3.")
    ]
)

def test_P2_2_19_menuOpciones(opcion, expected):
    assert menu_op(opcion) == expected