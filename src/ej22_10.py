
def pregunta_numero():
    """Solicita al usuario un número y lo devuelve como un entero."""
    return int(input("Introduce un número: "))

def es_primo(valor):
    """Devuelve True si el número es primo, de lo contrario False."""
    if valor < 2:  
        return False
    for i in range(2, int(valor**0.5) + 1):
        if valor % i == 0:
            return False
    return True

def main():
    n = pregunta_numero()
    
    if es_primo(n):
        print("El número es primo")
    else:
        print("El número no es primo")

if __name__ == "__main__":
    main()
