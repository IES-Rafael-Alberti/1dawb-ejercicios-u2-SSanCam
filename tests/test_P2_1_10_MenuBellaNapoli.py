import pytest 
from src.P2_1_10_MenuBellaNapoli import pedidoPizza

def test_pedir_pizza():
    assert pedidoPizza("v", 1) == "1.-Pimientos."
    assert pedidoPizza("v", 2) == "2.-Tofu."
    assert pedidoPizza("nv", 1) == "1.-Peperoni."
    assert pedidoPizza("nv", 2) == "2.-Jamón."
    assert pedidoPizza("nv", 3) == "3.-Salmón."