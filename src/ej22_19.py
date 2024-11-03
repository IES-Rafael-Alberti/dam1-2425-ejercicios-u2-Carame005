

def menu():
    """Muestra el menú y devuelve la opción seleccionada por el usuario."""
    print("\nMenu:")
    print("1. Comenzar programa")
    print("2. Imprimir listado")
    print("3. Finalizar Programa")
    try:
        p = int(input("Seleccione una opción: "))
        return p
    except ValueError:
        print("Opción inválida. Por favor, ingrese un número.")
        return None

def ejecutar_opcion(opcion):
    """Ejecuta la opción seleccionada y devuelve el mensaje correspondiente."""
    if opcion == 1:
        return "Programa iniciado"
    elif opcion == 2:
        return "Imprimiendo documentos"
    elif opcion == 3:
        return "Programa finalizado"
    else:
        return "Opción inválida"

def main():
    while True:
        opcion = menu()
        mensaje = ejecutar_opcion(opcion)
        print(mensaje)
        if opcion == 3:
            break

if __name__ == "__main__":
    main()
