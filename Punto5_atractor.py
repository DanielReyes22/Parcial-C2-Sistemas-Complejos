# Punto 5: Modelado Basado en Agentes (ABM) para Atractores 

import random

class Agente:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mover_hacia_atractor(self, atractor_x, atractor_y):
        # El agente ajusta su posición hacia el punto de equilibrio (atractor)
        self.x += (atractor_x - self.x) * 0.1
        self.y += (atractor_y - self.y) * 0.1

# Simulación simple
atractor = (50, 50)
agentes = [Agente(random.randint(0, 100), random.randint(0, 100)) for _ in range(5)]

print("Evolución de los agentes hacia el atractor:")
for i in range(3):
    print(f"Paso {i+1}:")
    for a in agentes:
        a.mover_hacia_atractor(*atractor)
        print(f"  Agente en: ({a.x:.2f}, {a.y:.2f})")