def menu():
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

def main():
    p = menu()
    while p != 3:
        if p == 1:
            print("Programa iniciado")
        elif p == 2:
            print("Imprimiendo documentos")
        else:
            print("Opción inválida") 
        p = menu()
    print("Programa finalizado")

if __name__ == "__main__":
    main()
