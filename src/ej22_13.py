def pedir_palabra():
    return input("Introduce cualquier cosa o 'salir' para terminar: ")


def main():
    palabra = pedir_palabra()
    while not palabra == "salir":
        print(palabra)
        palabra = pedir_palabra()
    print("Fin del programa")


if __name__ == "__main__":
    main()