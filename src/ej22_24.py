
def ingresa_numero():
    """Solicita al usuario un número y devuelve la entrada."""
    return input("Ingresa un número: ")

def es_primo(n):
    """Verifica si un número es primo."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    while True:
        try:
            n = int(ingresa_numero())
            if n == 0:
                break
            if es_primo(n):
                print(f"El número {n} es primo.")
            else:
                print(f"El número {n} no es primo.")
        except ValueError:
            print("Entrada no válida. Ingresa un número entero.")

if __name__ == "__main__":
    main()
