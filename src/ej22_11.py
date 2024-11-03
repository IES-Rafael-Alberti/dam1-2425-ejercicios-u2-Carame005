def introducir_palabra():
    return input("Introduce una palabra:")

def reverse_string(string):
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string

def main():
    palabra = introducir_palabra()
    palabra = reverse_string(palabra)
    for char in palabra:
        print(char)
    


if __name__ == '__main__':
    main()
    