
def ingresa_numero():
    return input("Ingrese un numero:")

def main():
    n = int(ingresa_numero())
    total = 0
    while not n == 0:
        if n < 0:
            print("No se puede ingresar un monto negativo.")
            n = int(ingresa_numero())
        else:
            total += n
            n = int(ingresa_numero())
    
    if total > 1000:
        descuento = total * 0.1
        total_pagar = total - descuento
        print(f"El total a pagar con descuento es :",total_pagar)
    else:
        print(f"El total a pagar es:",total)

if __name__ == "__main__":
    main()