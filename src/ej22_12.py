def pregunta_frase():
    return input("Dime una frase: ")

def pregunta_letra():
    return input("Dime una letra: ")


def main():
    frase = pregunta_frase()
    n = pregunta_letra()
    for letra_actual in frase:
        print(f"La letra {n} aparece {frase.count(n)} veces")
        break
    


if __name__ == "__main__":
    main()