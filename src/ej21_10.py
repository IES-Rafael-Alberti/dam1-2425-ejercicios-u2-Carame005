def preguntar_pizza():
    return input("¿Qué tipo de pizza quieres? (vegetariana, no vegetariana): ").lower()

def main():
    vegetariana = ["mozzarella", "tomate", "pimiento", "tofu"]
    no_vegetariana = ["mozzarella", "tomate", "peperoni", "jamón", "salmón"]
    
    pizza = preguntar_pizza()

    if pizza == "vegetariana":
        ingredientes = input("Dime qué único ingrediente quieres que lleve (pimiento, tofu): ").lower()
        if ingredientes == "pimiento":
            vegetariana.remove("tofu")  
        elif ingredientes == "tofu":
            vegetariana.remove("pimiento")
        print(f"Tu pizza vegetariana tiene {", ".join(map(str, vegetariana))}")
    
    elif pizza == "no vegetariana":
        ingredientes = input("Dime qué único ingrediente quieres que lleve (jamón, salmón, peperoni): ").lower()
        if ingredientes == "jamón":
            no_vegetariana.remove("salmón")
            no_vegetariana.remove("peperoni")
        elif ingredientes == "salmón":
            no_vegetariana.remove("jamón")
            no_vegetariana.remove("peperoni")
        elif ingredientes == "peperoni":
            no_vegetariana.remove("jamón")
            no_vegetariana.remove("salmón")
        print(f"Tu pizza no vegetariana tiene {", ".join(map(str, no_vegetariana))}")
    else:
        print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
