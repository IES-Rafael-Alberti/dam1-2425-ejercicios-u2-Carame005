from src.ej22_10 import es_primo
import pytest


def test_es_primo():
    """Prueba la función es_primo con varios números."""
    assert es_primo(1) == False  
    assert es_primo(2) == True  
    assert es_primo(3) == True   
    assert es_primo(4) == False  
    assert es_primo(17) == True  
    assert es_primo(18) == False  
    assert es_primo(19) == True  
    assert es_primo(25) == False  
