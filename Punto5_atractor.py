import random

class Estudiante:
    def __init__(self, id_estudiante):
        self.id = id_estudiante
        # Cada agente inicia con una nota aleatoria entre 0 y 5
        self.nota = random.uniform(0, 5)
        self.nueva_nota = self.nota

    def calcular_nueva_nota(self, todos_los_estudiantes, tolerancia):
        """
        Regla de interacción: El estudiante busca a otros con notas similares 
        (dentro de su grado de tolerancia) y calcula el promedio.
        """
        vecinos_validos = []
        
        for otro in todos_los_estudiantes:
            # Si la diferencia entre notas es menor o igual a la tolerancia, interactúan
            if abs(self.nota - otro.nota) <= tolerancia:
                vecinos_validos.append(otro.nota)
                
        # Calcula el promedio de las notas de su grupo de interacción
        if vecinos_validos:
            self.nueva_nota = sum(vecinos_validos) / len(vecinos_validos)

    def aplicar_cambio(self):
        # Actualiza la nota al mismo tiempo para que el orden de ejecución no afecte
        self.nota = self.nueva_nota

def simular_dinamica_notas():
    num_estudiantes = 20
    pasos_tiempo = 10
    tolerancia = 1.0  # Puedes cambiar esto a 0.5 (polarización) o 2.0 (consenso)
    
    # Crear los agentes (estudiantes)
    estudiantes = [Estudiante(i+1) for i in range(num_estudiantes)]

    print("--- INICIO DE SIMULACIÓN: ATRACTORES EMERGENTES (NOTAS) ---")
    print(f"Tolerancia configurada: {tolerancia}\n")

    # Evolución del sistema
    for t in range(pasos_tiempo):
        # 1. Todos calculan su nueva nota basándose en la tolerancia
        for e in estudiantes:
            e.calcular_nueva_nota(estudiantes, tolerancia)
            
        # 2. Todos aplican el cambio
        for e in estudiantes:
            e.aplicar_cambio()
            
        # Mostrar el estado del sistema cada ciertos pasos
        if t == 0 or t == pasos_tiempo - 1:
            notas_actuales = [round(e.nota, 2) for e in estudiantes]
            notas_actuales.sort() # Ordenamos para visualizar mejor los grupos
            print(f"Paso t={t+1}:")
            print(f"Notas: {notas_actuales}\n")

    print("--- FIN DE LA SIMULACIÓN ---")
    print("Observa cómo las notas convergen hacia valores específicos (Atractores Emergentes).")

if __name__ == "__main__":
    simular_dinamica_notas()
