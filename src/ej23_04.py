

def pide_numero():
    return input("Dame un  numero:")

def main():
    n = int(pide_numero())
    try:
        if n > 0 :
            print(n)
        if n < 0:
            raise ValueError("La entrada no es correcta")
    except ValueError as e:
        if n is None:
            print(f"Error: El numero introducido  no es un entero valido")
        else:
            print(f"Error: Ha ocurrido un error inesperado.{e}")

if __name__ == '__main__':
    main()