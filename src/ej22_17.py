def pedir_num():
    while True:
        try:
            numero = int(input("Dame un número entero positivo: "))
            if numero >= 0:
                return numero
            else:
                print("Por favor, introduce un número positivo.")
        except ValueError:
            print("Entrada inválida. Introduce un número entero.")

def main():
    numero = pedir_num()
    suma_digitos = sum(int(digito) for digito in str(numero))
    print("La suma de los dígitos es:", suma_digitos)

if __name__ == "__main__":
    main()
