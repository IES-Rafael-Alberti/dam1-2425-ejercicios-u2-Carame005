def preguntar_edad():
    return input("Dime tu edad: ")

def comprobar_numero(valor):
    try:
        numero = int(valor)
        if numero > 0:
            return True
        else:
            return False
    except ValueError:
        return ("Introduce una edad valida")

def main():
    n=preguntar_edad()
    cadena=[]
    while not comprobar_numero(n):
        n=preguntar_edad()
    for i in range(1, int(n)+1,):
        cadena.append(str(i))
    print( ",".join(cadena))
if __name__ == "__main__":
    main()