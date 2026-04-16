from functools import reduce

# 1. Definición del concepto de Interacción (Función f(Si, Sj))
# Representa cómo el estado del vecino j afecta al nodo i
def f_interaccion(estado_i, estado_j):
    intensidad = 0.6 
    return estado_j * intensidad

# 2. Definición de la Interacción Neta usando Programación Funcional
def calcular_interaccion_neta(estado_i, estados_vecinos):
    """
    Usa map para calcular cada interacción individual 
    y reduce para sumarlas todas (Net Interaction).
    """
    interacciones_individuales = map(lambda s_j: f_interaccion(estado_i, s_j), estados_vecinos)
    
    #obtener interaccion neta
    interaccion_neta = reduce(lambda acumulado, actual: acumulado + actual, interacciones_individuales, 0)
    
    return interaccion_neta

# --- Simulación ---
if __name__ == "__main__":
    estado_nodo_i = 1
    # Supongamos que tiene 3 vecinos con diferentes estados (cargas de datos o energía)
    estados_vecinos = [2.5, 3.0, 1.5] 

    neta = calcular_interaccion_neta(estado_nodo_i, estados_vecinos)
    nuevo_estado = estado_nodo_i + neta

    print(f"Estado original del nodo i: {estado_nodo_i}")
    print(f"Interaccion neta recibida: {neta}")
    print(f"Nuevo estado tras la interaccion: {nuevo_estado}")