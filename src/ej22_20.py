def pedir_letra():
    return input("Dame una letra: ")

def pedir_frase():
    return input("Dame una frase: ")

def main():
    letra = pedir_letra().lower() 
    frase = pedir_frase().lower() 
    
    for i, caracter in enumerate(frase): 
        if caracter == letra:
            print(f"Coincidencia encontrada en la posición {i}")
            break  
        else:
            print(f"No hay coincidencia en la posición {i}")

if __name__ == '__main__':
    main()
