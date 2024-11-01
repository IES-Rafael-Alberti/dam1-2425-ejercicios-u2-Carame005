def pregunta_numero():
    return int(input("Introduce un numero"))

def es_primo(valor):
    if valor % 1 == 0 and valor % valor == 0:
        return True
    else:
        return False
    

def main():
    n = pregunta_numero()
    
    if es_primo(n):
        print("El numero es primo")
    else:
        print("El numero no es primo")

if __name__ == "__main__":
    main()