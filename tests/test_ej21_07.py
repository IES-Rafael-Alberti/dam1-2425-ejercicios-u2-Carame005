from src.ej21_07 import comprobar_renta
import pytest


def test_comprobar_renta():
    assert comprobar_renta(5000) == "5%"      # Menor a 10,000
    assert comprobar_renta(15000) == "15%"    # Entre 10,000 y 20,000
    assert comprobar_renta(25000) == "20%"    # Entre 20,000 y 35,000
    assert comprobar_renta(40000) == "30%"    # Entre 35,000 y 60,000
    assert comprobar_renta(70000) == "40%"    # Mayor a 60,000
