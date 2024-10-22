#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
#El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un 
#nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario 
#su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

def comprobar_sexo():
    return input("Dame tu sexo (hombre/mujer): ").lower()

def comprobar_nombre():
    return input("Dame tu nombre: ").upper()

def main():
    sexo = comprobar_sexo()
    nombre = comprobar_nombre()
    
    if sexo == "mujer" and nombre[0] < "M":  
        print("Tu grupo es A")
    elif sexo == "hombre" and nombre[0] > "N": 
        print("Tu grupo es A")
    else:
        print("Tu grupo es B")

if __name__ == "__main__":
    main()
