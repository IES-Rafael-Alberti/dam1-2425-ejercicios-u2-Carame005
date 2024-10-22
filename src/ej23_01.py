def pedir_edad()->int:
    edad_incorrecta=True
    while edad_incorrecta:
        try:
            edad = int(input("Introduce tu edad"))
            
            if edad < 0:
                raise ValueError("La edad debe ser un numero positivo")
            if edad == 0:
                raise ValueError("La edad no puede ser 0")
            if edad > 125:
                raise ValueError("La edad no puede ser superior a 125")
            edad_incorrecta=False
        except ValueError as e:
            if edad is None:
                print(f"Error: El numero introducido  no es un entero valido")
            else:
                print(f"Error: Ha ocurrido un error inesperado.{(e)}")
    return edad


def mostrar_anios_cumplidos(edad: int):
    for i in range(1,edad +1):
        if i == edad:
            print(i)
        else:
            print (i,end=",")

def main():
        edad=pedir_edad()
        mostrar_anios_cumplidos(edad)


if __name__ == '__main__':
    main()