

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
    print(float(D/d))
    
if __name__ == "__main__":
    main()