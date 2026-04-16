# Parcial-C2-Sistemas-Complejos

1. La Complejidad de Internet: Un Enfoque Matemático
Para explicar por qué Internet es un sistema complejo no basaremos en el modelo de Redes de Escala Libre (Scale-Free Networks) el cuial se basa en la teoria de grafos.

El Modelo grafo
Podemos representar el Internet como un grafo $G = (V, E)$, el cual:

- $V$ (Vértices/Nodos): Son los routers, servidores o dispositivos finales.

- $E$ (Aristas/Enlaces): Son las conexiones físicas o lógicas entre ellos.

El Modelo: Ley de Potencia
A diferencia de las redes tradicionales, Internet no es aleatorio. Su estructura se define mediante una Ley de Potencia, expresada matemáticamente como:

$$P(k) \sim k^{-\gamma}$$

Donde: 

- $P(k)$: Es la probabilidad de que un nodo (un router o servidor) tenga $k$ conexiones.

- $\gamma$: Es un parámetro que en Internet suele oscilar entre 2 y 3.

¿Por qué esto explica su complejidad?

Este modelo matemático revela tres características fundamentales de la complejidad del sistema:

-Auto-Organización: El crecimiento de la red no es centralizado, es decir, los nuevos nodos tienden a conectarse a los nodos que ya estan conectados. 

-Robustez y Fragilidad: Por la ley de potencia el sistema es robusto ante fallos aleatorios por ende se explica el porque el internet es resistente a fallos accidentales. Pero su mayor vulnerabilidad son los ataques a los HUBS

-HUBS: La mayoria de los nodos tienen pocas conexiones; Caso aparte que hay unos pocos nodos (HUBS) que si tienen miles de conexiones. 






2. Aritmética Básica RecursivaSe implementó una lógica de computación básica utilizando la función sucesora $S(n) = n + 1$ como unidad fundamental de construcción.

Suma: Se define mediante la aplicación recursiva del sucesor de un número $a$, repetido $b$ veces.

Multiplicación: Utiliza la función de suma previamente construida para agregar un valor $a$ sobre sí mismo $b$ veces de forma recursiva





3. Modelo de Interacciones Netas (Programación Funcional)

Se modeló el concepto de Interacción Neta, que define cómo el estado de un elemento dentro de un sistema depende de la influencia agregada de su entorno.

Concepto Matemático: $I_{neta}(i) = \sum_{j \in Vecinos} f(S_i, S_j)$.

Implementación: Se aplicó programación funcional en Python, utilizando map para transformar los estados de los vecinos en interacciones individuales y reduce para realizar la sumatoria (agregación) total del efecto sobre el nodo.




4. La universalidad es una "Constante de la naturaleza" la cual establece que sistemas con detalles microscopicos que son completamente diferentes (atomos, neuronas, routers o personas) muestan el mismo comportamiento macroscopico cuando se acercan a un punto de transición o critico.
   
   -No importa el sistema como este hecho, si no como esta organizado.-
   
Desde el modelado computacional, la universalidad nos permite agrupar distintos problemas en clases de universalidad, es decir, para dinamica matematica se podria solucionar un problerma de fisica de particulas y un problema de logistica urbana, ya que se podria usar el mismo algoritmo para resolverlas 


Aplicación en un prbolema de ingenieria
Un problema critico puede ser la robustez en las redes de distribución(internet, elesctrica o agua)anste fallos masivos.


-Problema: Determinar el momento en que la red empiece a colapsar si los nodos fallan aleatoriamente.


-Modelo computacional (Percolación): La percolación estudia como cambia la conectividad de una red y sistemas complejos cuando se eliminan o añaden - nodos o enlaces de manera aleatoria o estrategica. Entonces en ves de modelar la ficia compleja de la electricidad o la presion del agua se usa este modelo.






5. Modelado Basado en Agentes (ABM): Atractores
Para este ejercicio, se implementó un modelo inspirado en la Confianza Limitada (Hegselmann-Krause), donde los agentes representan estudiantes con una calificación inicial aleatoria.

-Componentes del Modelo:

-Agentes: Estudiantes individuales con una "nota" (estado interno) entre 0 y 5.

-Estado Inicial: Caos total. Las notas están dispersas de forma aleatoria por todo el espacio de estados.

-Regla Local (Tolerancia): Un estudiante solo interactúa con otros cuyas notas sean similares a la suya (dentro de un rango de tolerancia $\epsilon$).

-Mecanismo de Adaptación: El agente ajusta su nota al promedio de su grupo de interacción.





