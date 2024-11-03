def pedir_num():
    """Solicita al usuario un número entero positivo."""
    while True:
        try:
            numero = int(input("Dame un número entero positivo: "))
            if numero >= 0:
                return numero
            else:
                print("Por favor, introduce un número positivo.")
        except ValueError:
            print("Entrada inválida. Introduce un número entero.")

def suma_digitos(numero):
    """Calcula la suma de los dígitos de un número entero positivo."""
    return sum(int(digito) for digito in str(numero))

def main():
    numero = pedir_num()
    resultado = suma_digitos(numero)
    print("La suma de los dígitos es:", resultado)

if __name__ == "__main__":
    main()
