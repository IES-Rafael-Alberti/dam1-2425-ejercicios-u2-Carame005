from src.ej21_04 import es_par
import pytest

def test_es_par():
    assert es_par(2) == True  # Caso: número par positivo
    assert es_par(4) == True  # Caso: otro número par positivo
    assert es_par(1) == False  # Caso: número impar positivo
    assert es_par(7) == False  # Caso: otro número impar positivo
    assert es_par(-2) == True  # Caso: número par negativo
    assert es_par(-3) == False  # Caso: número impar negativo
    assert es_par(0) == None  # Caso: número cero, retorna None según la lógica
