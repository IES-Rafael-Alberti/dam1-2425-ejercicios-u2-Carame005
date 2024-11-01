def ingresa_frase():
    return input("Ingrese una frase: ")

def main():
    frase = ingresa_frase()
    palabras = frase.split()  
    palabra_mas_larga = palabras[0]  

    for palabra in palabras:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra

    print("La palabra más larga es:", palabra_mas_larga)
    print("Número total de palabras:", len(palabras))

if __name__ == "__main__":
    main()
