# Parcial-C2-Sistemas-Complejos

1. La Complejidad de Internet: Un Enfoque Matemático
Para explicar por qué Internet es un sistema complejo no basaremos en el modelo de Redes de Escala Libre (Scale-Free Networks) el cuial se basa en la teoria de grafos.

El Modelo grafo
Podemos representar el Internet como un grafo $G = (V, E)$, el cual:

$V$ (Vértices/Nodos): Son los routers, servidores o dispositivos finales.

$E$ (Aristas/Enlaces): Son las conexiones físicas o lógicas entre ellos.

El Modelo: Ley de Potencia
A diferencia de las redes tradicionales, Internet no es aleatorio. Su estructura se define mediante una Ley de Potencia, expresada matemáticamente como:

$$P(k) \sim k^{-\gamma}$$

Donde: $P(k)$: Es la probabilidad de que un nodo (un router o servidor) tenga $k$ conexiones.

$\gamma$: Es un parámetro que en Internet suele oscilar entre 2 y 3.

¿Por qué esto explica su complejidad?

Este modelo matemático revela tres características fundamentales de la complejidad del sistema:

Auto-Organización: El crecimiento de la red no es centralizado, es decir, los nuevos nodos tienden a conectarse a los nodos que ya estan conectados. 

Robustez y Fragilidad: Por la ley de potencia el sistema es robusto ante fallos aleatorios por ende se explica el porque el internet es resistente a fallos accidentales. Pero su mayor vulnerabilidad son los ataques a los HUBS

HUBS: La mayoria de los nodos tienen pocas conexiones; Caso aparte que hay unos pocos nodos (HUBS) que si tienen miles de conexiones. 






2. Aritmética Básica RecursivaSe implementó una lógica de computación básica utilizando la función sucesora $S(n) = n + 1$ como unidad fundamental de construcción.

Suma: Se define mediante la aplicación recursiva del sucesor de un número $a$, repetido $b$ veces.

Multiplicación: Utiliza la función de suma previamente construida para agregar un valor $a$ sobre sí mismo $b$ veces de forma recursiva





3. Modelo de Interacciones Netas (Programación Funcional)

Se modeló el concepto de Interacción Neta, que define cómo el estado de un elemento dentro de un sistema depende de la influencia agregada de su entorno.

Concepto Matemático: $I_{neta}(i) = \sum_{j \in Vecinos} f(S_i, S_j)$.

Implementación: Se aplicó programación funcional en Python, utilizando map para transformar los estados de los vecinos en interacciones individuales y reduce para realizar la sumatoria (agregación) total del efecto sobre el nodo.





5. Modelado Basado en Agentes (ABM): Atractores
Se desarrolló un Modelamiento Basado en Agentes para ilustrar cómo surge el orden a partir de reglas locales simples, enfocándose en el concepto de Atractor.


Dinámica del Agente: Cada agente opera de forma autónoma y ajusta su posición actual en cada paso de tiempo hacia un punto de equilibrio estable.


Atractor de Punto Fijo: El sistema demuestra convergencia; independientemente de la posición aleatoria inicial, el sistema se auto-organiza hacia el estado estable definido en las coordenadas del atractor.





