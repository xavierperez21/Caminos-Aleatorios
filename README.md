# Caminos Aleatorios (ejemplo: camino de borrachos) 🍾

Este ejemplo es gracias al [Curso de Programación Dinámica y Estocástica en Python](https://platzi.com/cursos/programacion-estocastica/ "Curso de Programación Dinámica y Estocástica en Python") por parte de Platzi. 

El ejemplo se basa en los **Caminos Aleatorios**. Los caminos aleatorios es un tipo de simulación que elige aleatoriamente una decisión dentro de un conjunto de decisiones válidas.

Se utiliza en muchos campos del conocimiento cuando los sistemas no son deterministas e incluyen elementos de aleatoriedad. Como por ejemplo:
- El comportamiento de las galaxias.
- Fenomenos naturales (huracanes, tornados, temblores, etc).
- Pronóstico del clima.
...

En este ejemplo simularemos el caminar de un borracho *(en serio es muy aleatorio)*. El algoritmo consiste en situarnos en el origen de un plano cartesiano (x, y) y a partir de ahí tomar la decisión aleatoria de ir hacia arriba, abajo, a la izquierda o a la derecha. Todas con la misma probabilidad (25%).

Al final calcularemos la distancia final a donde termino nuestro camino aleatorio mediante la distancia euclidiana, la cual se deduce a partir del teorema de Pitágoras.

También se graficará (mediante la libreria **bokeh**) las estadísticas de la realización del algoritmo en diferente numero de pasos (10, 100, 1000, 10000) con un número de intentos (100). Esto con el objetivo de identificar cómo es que se comporta nuestro *borracho*, es decir, si conforme aumenta el número de pasos éste se aleja del origen o no.

<p align="center">
  <img src="./images/caminos_aleatorios_terminal.png" width="600" title="Terminal">
  <img src="./images/estadisticas.png" width="600" title="Estadisticas">
</p>

De igual manera se graficará a manera de ejemplo el camino que hizo el *borracho* sobre el plano cartesiano (x,y).

<p align="center">
  <img src="./images/ejemplo_de_camino.png" width="600" title="Ejemplo de camino">
</p>
