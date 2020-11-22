
# P000 - El número perdido

Una permutación de longitud $n$ es una lista $p = [p_1, p_2, \cdots, p_n]$ que
contiene todos los enteros de $1$ hasta $n$ sin que ninguno se encuentre
repetido. Por ejemplo, una permutation válida para $n = 5$ es
$p = [3, 4, 2, 1, 5]$.

En este problema tienes una permutación de entrada a la que le falta un solo
número.
Encuentra el número que falta en tiempo lineal y complejidad espacial constante.


## Entrada esperada:

La primera línea de entrada contiene un número entero $t$, el número de casos
de ejemplo. Por cada caso tenemos 2 líneas de entrada.

La primera línea del test es un número entero $n$, la longitud de la
permutación.
La segunda línea del test contiene una lista de enteros
$p_1, p_2, \cdots, p_{n-1} (1 \leq p_i \leq n)$, donde $p_i$ es el elemento $i$
de la lista $p$.


## Ejemplo:

Entrada:
```
2
5
3 2 1 5
10
1 2 3 4 5 6 7 8 9
```

Salida esperada:
```
4
10
```

