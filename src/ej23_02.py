def pide_numero():
    return input("Dame un numero: ")

def main():
    n = int(pide_numero())
    if n <= 0:
        print("Número denegado, debe ser positivo")
        return  
    else:
        cadena = []
        for i in range(1, n + 1, 2):
            cadena.append(str(i)) 
        print(", ".join(cadena))  
if __name__ == '__main__':
    main()
