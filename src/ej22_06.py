
def preguntar_numero():
    return int(input("Dime un número: "))

def main():
    n=preguntar_numero()
    
    for i in range(1,n,1):
        print("*" * i)

if __name__ == '__main__':
    main()