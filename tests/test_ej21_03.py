# test_ej21_03.py

from src.ej21_03 import comprobar_numero 
import pytest

def test_comprobar_numero():
    assert comprobar_numero(5) == True  # Caso: número distinto de cero
    assert comprobar_numero(0) == False  # Caso: número cero
    assert comprobar_numero(-3) == True  # Caso: número negativo distinto de cero
