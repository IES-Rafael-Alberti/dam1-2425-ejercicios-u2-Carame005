from src.ej21_09 import comprobar_edad
import pytest
def test_comprobar_edad():
    """Prueba la función comprobar_edad con diferentes edades."""
    assert comprobar_edad(3) == "Entras gratis"     # Menor de 4 años
    assert comprobar_edad(4) == "Precio: 5€"        # Entre 4 y 18 años
    assert comprobar_edad(18) == "Precio: 5€"       # Límite superior de 18 años
    assert comprobar_edad(19) == "Precio: 10€"      # Mayor de 18 años
    assert comprobar_edad(30) == "Precio: 10€"      # Edad mayor de 18 años
