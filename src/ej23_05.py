
def pide_contrasena():
    return input("Dame la contraseña:")

def main():
    n = pide_contrasena()
    n_new = pide_contrasena()
    try:
        if n_new == n  :
            print("La contraseña es correcta")
        if not n_new == n :
            raise ValueError("Incorrect Password!!")
    except ValueError as e:
        if n is None:
            print(f"Error: El valor introducido  no es un valor valido")
        else:
            print(f"Error: Ha ocurrido un error inesperado.{e}")

if __name__ == '__main__':
    main()