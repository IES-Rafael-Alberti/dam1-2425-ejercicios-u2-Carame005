from src.ej22_17 import suma_digitos
import pytest

def test_suma_digitos():
    """Prueba la función suma_digitos con diferentes números."""
    assert suma_digitos(123) == 6      
    assert suma_digitos(4567) == 22   
    assert suma_digitos(9999) == 36    
    assert suma_digitos(1001) == 2     
