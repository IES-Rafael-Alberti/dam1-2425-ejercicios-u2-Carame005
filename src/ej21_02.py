
def main():
    contraseña=input("Ingrese la contraseña.").lower()
    print("Contraseña guardada correctamente.")
    contraseña1=input("¿Que contraseña puso?").lower()
    while contraseña1 != contraseña:
        print("Contraseña incorrecta. Inténtelo de nuevo.")
        contraseña1=input("¿Que contraseña puso?")
    print("Contraseña correcta.")
if __name__ == "__main__":
    main()