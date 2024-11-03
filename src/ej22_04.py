
def preguntar_numero():
    return input("Dime un número: ")

def comprobar_numero(valor):
    try:
        numero = int(valor)
        if numero > 0:
            return True
        else:
            return False
    except ValueError:
        return ("Introduce un valor valido")

def main():
    n=preguntar_numero()
    cadena=[]
    while not comprobar_numero(n):
        n=preguntar_numero() 
    for i in range(int(n), -1, -1,):
        cadena.append(str(i))
    print( "+".join(cadena))
    cadena=[]
    for i in reversed (range(int(n)+1)):
        cadena.append(str(i))
    print( ",".join(cadena))
if __name__ == "__main__":
    main()
    
    
    