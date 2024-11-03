def ingresa_frase():
    """Solicita al usuario que ingrese una frase y la devuelve."""
    return input("Ingrese una frase: ")

def obtener_palabra_mas_larga_y_conteo(frase):
    """
    Encuentra la palabra más larga y cuenta el número de palabras en una frase.
    
    Args:
        frase (str): La frase ingresada por el usuario.
        
    Returns:
        tuple: Una tupla que contiene la palabra más larga (str) y el conteo total de palabras (int).
    """
    palabras = frase.split()
    palabra_mas_larga = palabras[0] if palabras else ""

    for palabra in palabras:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra

    return palabra_mas_larga, len(palabras)

def main():
    frase = ingresa_frase()
    palabra_mas_larga, total_palabras = obtener_palabra_mas_larga_y_conteo(frase)
    print("La palabra más larga es:", palabra_mas_larga)
    print("Número total de palabras:", total_palabras)

if __name__ == "__main__":
    main()
