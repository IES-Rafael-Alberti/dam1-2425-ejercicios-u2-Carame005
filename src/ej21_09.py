def comprobar_edad(edad):
    if edad < 4:
        return print("Entras gratis")
    else:
        if edad >= 4 and edad <= 18:
            return print("Precio: 5€")
        else:
            return print("Precio: 10€")

def main():
    edad=int(input("Dame tu edad"))
    comprobar_edad(edad)


if __name__ == '__main__':
    main()