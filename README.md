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
