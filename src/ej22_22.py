
def pedir_numero():
    return input("Dame un numero:")


def main():
    n = int(pedir_numero())
    while not n == 0:
        if n < 0:
            print("El numero debe ser positivo")
        else:
            digitos = len(str(n))
            pares = sum(int(digit) % 2 == 0 for digit in str(n))
            impares = sum(int(digit) % 2!= 0 for digit in str(n))
            print(f"El numero {n} tiene {digitos} digitos, de los cuales {pares} son pares y {impares} son impares")
            n = int(pedir_numero())

if __name__ == "__main__":
    main()