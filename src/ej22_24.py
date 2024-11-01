def ingresa_numero():
    return input("Ingresa un numero:")
def main():
    n = int(ingresa_numero())
    while n != 0:
        if int(n) > 1:
            for i in range(2, int(n)):
                if (int(n) % i) == 0:
                    break
            else:
                print("El numero", n, "es primo.")
        n = int(ingresa_numero())

if __name__ == "__main__":
    main()