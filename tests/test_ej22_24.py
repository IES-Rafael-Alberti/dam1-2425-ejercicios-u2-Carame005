from src.ej22_24 import es_primo
import pytest


def test_es_primo():
    """Prueba la función es_primo con varios valores."""
    assert es_primo(2) == True         
    assert es_primo(3) == True         
    assert es_primo(4) == False      
    assert es_primo(29) == True       
    assert es_primo(1) == False        
    assert es_primo(0) == False      
    assert es_primo(-5) == False     
