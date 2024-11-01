#Crear un programa que permita al usuario ingresar títulos de libros por teclado, 
# finalizando el ingreso al leerse el string “*” (asterisco). 
# Cada vez que el usuario ingrese un string de longitud 1 que contenga sólo una barra (“/”) 
# se considera que termina una línea. Por cada línea completa, informar cuántos dígitos numéricos
# (del 0 al 9) aparecieron en total (en todos los títulos de libros que componen en esa línea). 
# Finalmente, informar cuántas líneas completas se ingresaron.

def ingresa_titulo():
    return input("Ingrese el titulo:")

def main():
    title = ingresa_titulo()
    titles = []
    line_count = 0
    while title != "*":
        if title == "/ ":
            line_count += 1
            print("Cantidad de digitos numericos:", sum(c.isdigit() for c in title))
            print("Cantidad de lineas completas:", (line_count))
            titles = []
        else:
            titles.append(title)
        title = ingresa_titulo()

if __name__ == "__main__":
    main()
