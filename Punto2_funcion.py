
# PUNTO 2: ARITMÉTICA BÁSICA RECURSIVA

def S(n):
    """
    Función sucesora
    S(n) = n + 1
    """
    return n + 1

def sumar(a, b):
    """
    Lógica: Se aplica el sucesor de 'a', 'b' veces.
    """
    if b == 0:
        return a
    return S(sumar(a, b - 1))

def multiplicar(a, b):
    """
    Lógica: Se suma 'a' a sí mismo 'b' veces.
    """
    if b == 0:
        return 0
    return sumar(a, multiplicar(a, b - 1))



if __name__ == "__main__":
    print("--- Resultados del Punto 2 ---")
    
    # Ejemplo 1
    ej1_sum = sumar(10, 5)
    print(f"1. Suma (10 + 5) = {ej1_sum}")

    # Ejemplo 2
    ej2_mult = multiplicar(2, 4)
    print(f"2. Multiplicación (2 * 4) = {ej2_mult}")

    # Ejemplo 3
    ej3_sum = sumar(0, 7)
    print(f"3. Suma con cero (0 + 7) = {ej3_sum}")

    # Ejemplo 4
    ej4_mult = multiplicar(6, 1)
    print(f"4. Multiplicación por uno (6 * 1) = {ej4_mult}")

    # Ejemplo 5
    ej5_mult = multiplicar(0, 5)
    print(f"5. Multiplicación por cero (0 * 5) = {ej5_mult}")