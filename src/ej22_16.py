def main(): 
    mayor_numero = 0

    while True:
        numero = int(input("Introduce un número entero positivo (0 para terminar): "))
        if numero == 0:
            break
        if numero > mayor_numero:
            mayor_numero = numero
    print("El mayor número ingresado fue:", mayor_numero)
