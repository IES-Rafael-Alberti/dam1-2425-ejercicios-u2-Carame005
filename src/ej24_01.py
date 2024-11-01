def main():
    """
    Función principal que ejecuta el algoritmo de ordenamiento burbuja para un arreglo de números.

    Este algoritmo recorre repetidamente el arreglo, comparando elementos adyacentes y 
    los intercambia si están en el orden incorrecto. Al final, el arreglo queda ordenado 
    de menor a mayor.

    Args:
        No recibe ningún argumento de entrada.

    Returns:
        No devuelve ningún valor, pero imprime el arreglo ordenado.
    """
    a = [8, 3, 1, 19, 14]
    n = len(a)  

    
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:  
                a[j], a[j + 1] = a[j + 1], a[j]
    
    print("Arreglo ordenado:", a)  

if __name__ == '__main__':
    main()
