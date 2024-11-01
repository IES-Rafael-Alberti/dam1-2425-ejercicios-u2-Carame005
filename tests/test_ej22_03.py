from src.ej22_03 import comprobar_numero 
import pytest

def test_comprobar_numero():
    """Prueba la función comprobar_numero con diferentes valores de entrada."""
    assert comprobar_numero("10") == True        # Número entero positivo
    assert comprobar_numero("0") == False        # Número cero
    assert comprobar_numero("-5") == False       # Número negativo
    assert comprobar_numero("abc") == False      # Cadena no numérica
    assert comprobar_numero("5.5") == False      # Número decimal en cadena
