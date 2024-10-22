#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
def es_par(n):
    if (n % 2 == 0) and n != 0:
        return True
    if (n % 2 == 1) and n != 0:
        return False
def main():
    n=int(input("Dime un numero"))
    if n == 0:
        print("El numero introducido es 0,no es par ni impar")
    elif es_par(n):
        print(f"{n} es par")
    elif not es_par(n):
        print(f"{n} es impar")

if __name__ == '__main__':
    main()