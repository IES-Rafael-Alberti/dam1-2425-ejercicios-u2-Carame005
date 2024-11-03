def comprobar_numero(num:int)-> bool:
    if num > 0:
        return "Positivo"
    elif num < 0:
        return "Negativo"
    else:
        return "Cero"

def intro_numero(msj:str)-> int:
    valor=input(msj).strip()
    
    if comprobar_numero(valor) == True:
        return int(valor)
    elif valor.lower() == "fin":
        return -1
    else:
        return -2
    
def main():
    
    cantidad = 0
    suma = 0
    media = 0
    salir = False
    
    while not salir:
        entrada = int(input("Introduce un numero"))
        if entrada == 1:
            salir = True
        elif entrada is None:
            print("Entrada invalida")
        else:
            cantidad += 1
            suma += entrada
        
    media= suma / cantidad
    print(f"{9}{9}{0}")
    
if __name__ == "__main__":
    main()