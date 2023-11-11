import pytest 
from src.P2_1_7_declaracionRenta import declaracion

def test_declaracion_renta():
    assert declaracion(900) == "5%"
    assert declaracion(11000) == "15%"
    assert declaracion(21000) == "20%"
    assert declaracion(35000) == "30%"
    assert declaracion(62000) == "45%"

@pytest.mark.parametrize(
    "renta, expected",
    [
        (900, "5%"),
        (12000, "15%"),
        (25000, "20%"),
        (36000, "30%"),
        (123234, "45%")
    ]
)

def test_P2_1_7_declaracionRenta(renta, expected):
    assert declaracion(renta) == expected