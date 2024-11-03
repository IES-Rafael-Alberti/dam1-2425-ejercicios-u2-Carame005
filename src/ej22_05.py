def preguntar_cantidad():
    return float(input("¿Cuanto dinero desea invertir? "))

def preguntar_interes():
    return float(input("¿Cual es el interes anual? "))

def preguntar_anios():
    return int(input("¿Cuantos años desea invertir? "))

def main():
    amount = preguntar_cantidad()
    interest = preguntar_interes()
    anios = preguntar_anios()
    for i in range(0,anios):
        amount *= 1 + interest / 100
        print(f"En el año {i} usted ganó {amount}€")

if __name__ == "__main__":
    main()