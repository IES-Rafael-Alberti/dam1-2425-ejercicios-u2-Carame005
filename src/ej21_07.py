

def comprobar_renta(valor):
    """Devuelve el porcentaje de renta en función del valor."""
    if valor < 10000:
        return "5%"
    elif valor >= 10000 and valor < 20000:
        return "15%"
    elif valor >= 20000 and valor < 35000:
        return "20%"
    elif valor >= 35000 and valor <= 60000:
        return "30%"
    elif valor > 60000:
        return "40%"

def main():
    renta = int(input("Dime tu renta: "))
    print(comprobar_renta(renta))

if __name__ == "__main__":
    main()
