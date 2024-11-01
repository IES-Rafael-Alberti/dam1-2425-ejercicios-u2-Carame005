def main():
    a = [8, 3, 1, 19, 14]
    n = len(a)
    for i in range( 0,n-1):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

if __name__ == '__main__':
    main()