
def pedir_num():
    return int(input("Dame un número entero positivo: "))

def main():
    numero = pedir_num()
    par = 0
    while not numero == -1:
        suma_digitos = sum(int(digito) for digito in str(numero))
        print("La suma de los dígitos es:", suma_digitos)
        if numero % 2 == 0:
            par += 1
        numero = pedir_num()
    print("Cantidad de números pares ingresados:", par)

if __name__ == "__main__":
    main()
