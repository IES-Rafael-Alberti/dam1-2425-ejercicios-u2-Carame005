
def comprobar_edad(edad):
    """Devuelve el precio de entrada basado en la edad."""
    if edad < 4:
        return "Entras gratis"
    elif 4 <= edad <= 18:
        return "Precio: 5€"
    else:
        return "Precio: 10€"

def main():
    edad = int(input("Dame tu edad: "))
    print(comprobar_edad(edad))

if __name__ == '__main__':
    main()
