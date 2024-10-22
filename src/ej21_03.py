#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
#Si el divisor es cero el programa debe mostrar un error.

def comprobar_numero(valor):
    if valor == 0:
        return False
    else:
        return True
def main():
    D=int(input("Introduzca el dividendo"))
    d=int(input("Introduzca el divisor"))
    while not comprobar_numero(d):
        print("Error: El divisor no puede ser cero")
        d=int(input("Introduzca el divisor"))
    print(f"La deivision de {D} entre {d} es {float(D/d)}")
    
if __name__ == "__main__":
    main()