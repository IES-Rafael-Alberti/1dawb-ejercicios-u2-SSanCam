import pytest
from src.P2_1_8_rendimientoAnual import evaluacionAnual

@pytest.mark.parametrize(
    "puntuacion, expected",
    [
        (0.0, "0.00€"),
        (0.4, "960.00€"),
        (0.6, "1440.00€")
    ]
)

def test_P2_1_8_rendimientoAnual(puntuacion, expected):
    assert evaluacionAnual(puntuacion) == expected