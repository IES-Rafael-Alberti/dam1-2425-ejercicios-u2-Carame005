def preguntar_numero():
    return int(input("Dime un número: "))



def main():
    n=preguntar_numero()
    cadena = []
    cadena.append(1)
    for i in range(1,n,2):
        print(f"{", ".join(map(str, cadena))}")
        cadena.append(i+2)
        


if __name__ == '__main__':
    main()