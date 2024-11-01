def preguntar_numero():
    return input("Dime un número: ")

def comprobar_numero(valor):
    """Verifica si el valor ingresado es un número entero positivo."""
    try:
        numero = int(valor)
        return numero > 0
    except ValueError:
        return False

def preguntar_numero():
    """Solicita al usuario un número entero positivo."""
    return input("Dame un número: ")

def main():
    n = preguntar_numero()
    cadena = []

    while not comprobar_numero(n):
        print("Introduce un valor válido")
        n = preguntar_numero()

    for i in range(1, int(n) + 1, 2):
        cadena.append(str(i))

    print(",".join(cadena))

if __name__ == "__main__":
    main()
