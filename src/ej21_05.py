#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener 
#unos ingresos iguales o superiores a 1000 € mensuales. 
#Escribir un programa que pregunte al usuario su edad y 
#sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

def es_mayor_de_edad(edad):
    if edad<16:
        return False
    else:
        return True
    
def comprobar_ingresos(ingresos):
    if ingresos<1000:
        return False
    else:
        return True
    
def main():
    edad = int(input("Introduce tu edad: "))
    ingresos = float(input("Introduce tus ingresos mensuales: "))
    if es_mayor_de_edad(edad) and comprobar_ingresos(ingresos):
        print("Usted tiene que tributar.")
    else:
        print("Usted no tiene que tributar.")

if __name__ == "__main__":
    main()