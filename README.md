# Diferencia de rendimiento entre C y Python

## 1. Descripción

Este proyecto presenta un experimento para observar la diferencia de
rendimiento entre una implementación en C y una implementación en Python
del mismo problema numérico.

El problema elegido es el cálculo de la suma de la serie armónica:

S(n) = 1 + 1/2 + 1/3 + ... + 1/n

La elección permite mantener el algoritmo sencillo y concentrar la
comparación en el tiempo de ejecución de los dos lenguajes.

El experimento se ejecutó en Ubuntu Linux dentro de VirtualBox. Las
versiones utilizadas fueron Python 3.14.4, GCC 15.2 y Matplotlib. No se
registró en esta ejecución el modelo del procesador ni la cantidad de
memoria asignada a la máquina virtual, por lo que no se inventan esos
datos.

## 2. Objetivo

Diseñar un experimento que permita observar la diferencia de rendimiento
entre C y Python al resolver el mismo problema numérico bajo las mismas
condiciones generales de ejecución.

## 3. Problema numérico

Para un valor n se calcula:

S(n) = sumatorio desde i=1 hasta n de 1/i

Por ejemplo, para n = 4:

S(4) = 1 + 1/2 + 1/3 + 1/4

El algoritmo utiliza un ciclo que recorre los valores desde 1 hasta n.

### Complejidad

El algoritmo tiene:

-   Complejidad temporal: O(n)
-   Complejidad espacial: O(1)

La complejidad es la misma en C y Python. Por tanto, el experimento
permite separar la idea de complejidad algorítmica de la diferencia de
costo de ejecución de cada lenguaje.

## 4. Diseño experimental

Se probaron cinco tamaños:

             n        C (s)   Python (s)   Python/C
  ------------ ------------ ------------ ----------
     1.000.000     0.001897   0.02480085      13.07
     2.000.000     0.002710   0.05314333      19.61
     5.000.000     0.006134   0.12278272      20.02
    10.000.000   0.01010833   0.23773077      23.52
    20.000.000     0.022954   0.46342667      20.18

Cada tamaño se ejecuta tres veces por lenguaje y se utiliza el promedio
de los tiempos.

La variable independiente es n, es decir, la cantidad de términos de la
serie.

La variable dependiente es el tiempo de ejecución.

El factor Python/C se calcula como:

factor = tiempo de Python / tiempo de C

Por ejemplo, para 20.000.000:

0.46342667 / 0.022954 = 20.18 aproximadamente.

Esto significa que Python tardó aproximadamente 20,18 veces el tiempo de
C en esa prueba.

## 5. Control de la comparación

Las implementaciones utilizan el mismo procedimiento:

1.  Inicializar la suma en cero.
2.  Recorrer desde 1 hasta n.
3.  Calcular 1/i.
4.  Acumular el valor.
5.  Medir el tiempo de cálculo.

No se utiliza NumPy ni una biblioteca numérica para realizar el cálculo.
Esto evita delegar el trabajo principal a código compilado externo y
permite comparar las operaciones realizadas por cada implementación.

El tiempo medido corresponde al cálculo de la suma. El inicio del
cronómetro se realiza después de recibir el valor n y antes del ciclo
principal.

En C se utiliza la compilación con:

gcc -O2

En Python se utiliza CPython mediante el comando python3.

## 6. Resultados numéricos

Los resultados de C y Python fueron iguales en las cinco pruebas. La
columna `diferencia_numerica` del CSV fue 0.0 para todos los tamaños.

Esto permite comprobar que la diferencia de rendimiento no proviene de
que una implementación esté resolviendo un problema diferente.

Los factores observados fueron:

-   1.000.000 términos: Python tardó 13,07 veces el tiempo de C.
-   2.000.000 términos: Python tardó 19,61 veces el tiempo de C.
-   5.000.000 términos: Python tardó 20,02 veces el tiempo de C.
-   10.000.000 términos: Python tardó 23,52 veces el tiempo de C.
-   20.000.000 términos: Python tardó 20,18 veces el tiempo de C.

El factor no es exactamente constante. Esto es esperable en una medición
realizada sobre un computador real, especialmente dentro de una máquina
virtual, porque existen variaciones asociadas al sistema y a la
ejecución.

## 7. Gráficas

La gráfica principal es:

`graficas/comparacion_rendimiento.png`

También se incluye una versión con escala logarítmica:

`graficas/comparacion_rendimiento_log.png`

La escala logarítmica permite visualizar mejor la variación de C porque
sus tiempos son mucho menores que los de Python.

En la gráfica lineal, la línea de C parece estar muy cerca de cero, pero
no es cero. Sus tiempos son simplemente mucho menores que los de Python.

## 8. Análisis

Los resultados muestran que C obtuvo el menor tiempo de ejecución en
todas las pruebas.

La diferencia se vuelve evidente desde el primer tamaño. Con un millón
de términos, C tardó aproximadamente 0,001897 segundos mientras Python
tardó aproximadamente 0,024801 segundos.

Al aumentar n, el tiempo aumenta en ambos lenguajes porque ambos
ejecutan un número proporcional de iteraciones. Esto coincide con la
complejidad O(n).

Sin embargo, tener la misma complejidad no significa tener el mismo
tiempo real. O(n) describe cómo crece el costo del algoritmo con
respecto al tamaño de entrada, pero no indica cuánto cuesta cada
operación.

En este experimento, C se compila previamente y el procesador ejecuta
instrucciones generadas por el compilador. En CPython, el programa pasa
por una etapa de traducción a bytecode y posteriormente ese bytecode es
ejecutado por el entorno de ejecución de Python. Esto introduce trabajo
adicional en un ciclo con millones de operaciones simples.

El resultado no significa que C sea siempre una cantidad fija de veces
más rápido que Python. El factor depende del problema, la
implementación, el compilador, la versión del intérprete y las
condiciones del equipo.

## 9. Conclusión

El experimento permite validar una diferencia de rendimiento entre las
dos implementaciones.

Para el problema de la suma de la serie armónica, C obtuvo tiempos
menores que Python en los cinco tamaños evaluados. Python presentó
tiempos entre 13,07 y 23,52 veces mayores que C según el tamaño de
entrada.

Ambas implementaciones tienen la misma complejidad temporal O(n) y
produjeron los mismos resultados numéricos. Por lo tanto, la diferencia
observada no se explica por una diferencia en el algoritmo, sino por el
costo de ejecución asociado a cada implementación y al entorno
utilizado.

La conclusión debe limitarse a las condiciones de este experimento. No
se puede afirmar a partir de estas pruebas que C sea siempre más rápido
que Python en cualquier programa.

## 10. Requisitos

Se necesita:

-   Python 3
-   GCC
-   Matplotlib

En Ubuntu se pueden comprobar con:

``` bash
python3 --version
gcc --version
python3 -c "import matplotlib; print(matplotlib.__version__)"
```

## 11. Ejecución

Desde la carpeta principal:

``` bash
python3 src/experimento.py
```

Este comando compila el programa de C con `-O2`, ejecuta las pruebas
tres veces para cada tamaño y actualiza `resultados/resultados.csv`.

Para generar las gráficas:

``` bash
python3 graficas/graficar_resultados.py
```

## 12. Estructura del proyecto

``` text
Tarea_1_Lenguajes/
├── README.md
├── requirements.txt
├── src/
│   ├── suma_armonica.c
│   ├── suma_armonica.py
│   └── experimento.py
├── resultados/
│   └── resultados.csv
├── graficas/
│   ├── graficar_resultados.py
│   ├── comparacion_rendimiento.png
│   └── comparacion_rendimiento_log.png

## 13. Nota sobre reproducibilidad

Los resultados incluidos en `resultados/resultados.csv` corresponden a
la ejecución realizada en Ubuntu Linux dentro de VirtualBox durante el
desarrollo de este trabajo.

Si el experimento se ejecuta nuevamente, los tiempos pueden cambiar. Lo
esperado es conservar la tendencia general, pero no necesariamente los
mismos valores exactos.

Para una nueva medición se recomienda cerrar programas innecesarios,
mantener las mismas cantidades de n y utilizar las mismas opciones de
compilación.
