def comprobar_renta(valor):
    if valor < 10000:
        return print("5%")
    elif valor >= 10000 and valor < 20000:
        return print("15%")
    elif valor >= 20000 and valor < 35000:
        return print("20%")
    elif valor >= 35000 and valor <= 60000:
        return print("30%")
    elif valor > 60000:
        return print("40%")

def main():
    renta=int(input("Dime tu renta"))
    comprobar_renta(renta)

if __name__ == "__main__":
    main()