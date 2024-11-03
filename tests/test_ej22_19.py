from src.ej22_19 import ejecutar_opcion
import pytest

def test_ejecutar_opcion():
    """Prueba la función ejecutar_opcion con diferentes opciones."""
    assert ejecutar_opcion(1) == "Programa iniciado"         
    assert ejecutar_opcion(2) == "Imprimiendo documentos"     
    assert ejecutar_opcion(3) == "Programa finalizado"   
    assert ejecutar_opcion(4) == "Opción inválida"      
    assert ejecutar_opcion(None) == "Opción inválida"        
