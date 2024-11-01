def pedir_contraseña():
    return input("Dame la contraseña")

def main():
    contraseña = pedir_contraseña()
    print("Contraseña guardada correctamente.")
    contraseña1 = pedir_contraseña()
    while contraseña1 != contraseña:
        print("Contraseña incorrecta. Inténtelo de nuevo.")
        contraseña1 = pedir_contraseña()
    print("Contraseña correcta.")
if __name__ == "__main__":
    main()