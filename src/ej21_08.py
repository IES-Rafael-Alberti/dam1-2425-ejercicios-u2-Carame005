def calcular_puntuacion(valor):
    return 2400 * valor

def main():
    valor_texto = {
        0.0: "rendimiento inaceptable",
        0.4: "rendimiento aceptable",
        0.6: "rendimiento meritorio",
        0.8: "rendimiento inmejorable",
        1.0: "rendimiento excelente"
    }

    Puntos = float(input("Introduce un valor (0.0, 0.4, 0.6, 0.8, 1.0): "))
    puntuacion = calcular_puntuacion(Puntos)

    if Puntos in valor_texto:
        print(f"Tus ingresos son de: {puntuacion} € y tu {valor_texto[Puntos]}")
    else:
        print("Valor no válido.")

if __name__ == "__main__":
    main()
