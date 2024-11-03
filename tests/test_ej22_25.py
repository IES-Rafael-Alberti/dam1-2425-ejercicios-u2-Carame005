from src.ej22_25 import obtener_palabra_mas_larga_y_conteo
import pytest

def test_obtener_palabra_mas_larga_y_conteo():
    """Prueba la función obtener_palabra_mas_larga_y_conteo con diferentes frases."""
    assert obtener_palabra_mas_larga_y_conteo("La casa es grande") == ("grande", 4)
    assert obtener_palabra_mas_larga_y_conteo("Python es divertido") == ("divertido", 3)
    assert obtener_palabra_mas_larga_y_conteo(" ") == ("", 0)  
    assert obtener_palabra_mas_larga_y_conteo("Hola mundo") == ("mundo", 2)
    assert obtener_palabra_mas_larga_y_conteo("Un solo") == ("solo", 2)

