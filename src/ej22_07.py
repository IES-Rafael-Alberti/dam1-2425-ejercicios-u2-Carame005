def main():
    cont=1
    while not cont > 10:
        for i in range(1,11):
            print(f"{cont}*{i} = {cont*i}")
        cont += 1
if __name__ == '__main__':
    main()