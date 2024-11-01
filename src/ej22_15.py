def ingresa_numero():
    return int(input("Ingresa un numero"))



def main():
    n = ingresa_numero()
    cont = 0
    while not n == 0:
        if n > 0:
            cont = cont + n
        n = ingresa_numero()
    print(cont)


if __name__ == '__main__':
    main()