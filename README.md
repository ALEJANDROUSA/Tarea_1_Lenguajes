# Diferencia de rendimiento entre C y Python

## 1. Descripción

Este proyecto presenta un experimento para observar la diferencia de rendimiento entre C, un lenguaje compilado, y Python, que normalmente se ejecuta mediante CPython.

El problema numérico elegido es la suma de la serie armónica:

S(n) = 1 + 1/2 + 1/3 + ... + 1/n

La misma lógica se implementa en C y Python. No se utiliza NumPy ni otra biblioteca numérica externa para realizar el cálculo, porque el objetivo es comparar directamente la ejecución del algoritmo en ambos lenguajes.

## 2. Objetivo

Diseñar un experimento que permita observar cómo cambia el tiempo de ejecución de un mismo algoritmo numérico al implementarlo en C y Python.

## 3. Problema

Para un valor n, se calcula:

S(n) = sumatorio desde i=1 hasta n de 1/i

El algoritmo utiliza un único ciclo, por lo que su complejidad temporal es O(n) y su complejidad espacial es O(1).

## 4. Diseño experimental

Se utilizan los siguientes tamaños:

- 1.000.000
- 2.000.000
- 5.000.000
- 10.000.000
- 20.000.000

Cada tamaño se ejecuta tres veces en cada lenguaje. Se utiliza el promedio de los tiempos.

La variable independiente es n y la variable dependiente es el tiempo de ejecución.

El factor de comparación es:

factor = tiempo de Python / tiempo de C

Si el factor es 10, Python tardó aproximadamente diez veces el tiempo de C para esa prueba.

## 5. Control de la comparación

Las dos implementaciones utilizan el mismo algoritmo:

1. Inicializar la suma en cero.
2. Recorrer desde 1 hasta n.
3. Calcular 1/i.
4. Acumular el resultado.
5. Medir el tiempo.

No se utiliza NumPy porque sus operaciones numéricas delegan gran parte del trabajo en código compilado y optimizado, lo que cambiaría el objetivo de la comparación.

## 6. Estructura

```text
diferencia_c_vs_python/
├── README.md
├── requirements.txt
├── src/
│   ├── suma_armonica.c
│   ├── suma_armonica.py
│   └── experimento.py
├── resultados/
│   └── resultados.csv
└── graficas/
    └── graficar_resultados.py
```

Después de ejecutar la graficación aparecerá `graficas/comparacion_rendimiento.png`.

## 7. Requisitos

Se necesita Python 3, GCC y Matplotlib.

Comprobar Python:

```bash
python --version
```

Comprobar GCC:

```bash
gcc --version
```

Instalar Matplotlib:

```bash
python -m pip install matplotlib
```

## 8. Ejecución

Desde la carpeta principal:

```bash
python src/experimento.py
```

El experimento compila C, ejecuta C y Python para cada tamaño, repite las pruebas tres veces, calcula los promedios y guarda los datos en `resultados/resultados.csv`.

Después:

```bash
python graficas/graficar_resultados.py
```

La gráfica se guardará como `graficas/comparacion_rendimiento.png`.

## 9. Compilación de C

El experimento utiliza:

```bash
gcc -O2 src/suma_armonica.c -o src/suma_armonica
```

En Windows normalmente se genera `suma_armonica.exe`.

`-O2` activa optimizaciones comunes del compilador para mejorar el rendimiento sin cambiar el resultado del programa.

## 10. Resultados

Los tiempos dependen del computador donde se ejecute el experimento. Por ello, los resultados definitivos deben obtenerse en el equipo utilizado para la entrega.

El CSV contiene:

- n
- tiempo de C
- tiempo de Python
- factor Python/C
- resultado de C
- resultado de Python
- diferencia numérica

También se comprueba que ambos programas produzcan resultados prácticamente iguales.

## 11. Análisis

Ambos programas tienen complejidad O(n), pero esto no implica que tarden exactamente lo mismo. La complejidad describe cómo crece el costo con respecto a la entrada, mientras que el tiempo real también depende del costo de ejecutar cada operación.

C se compila antes de ejecutarse y el código generado puede ser ejecutado directamente por el procesador.

En CPython, el código fuente se transforma en bytecode y posteriormente es ejecutado por la máquina virtual de Python. Esto introduce trabajo adicional en cada iteración.

Por eso, para un cálculo formado por millones de operaciones simples, se espera una diferencia de rendimiento entre ambas implementaciones.

## 12. Conclusión

La conclusión definitiva debe construirse con los resultados obtenidos en el computador donde se realice el experimento.

Debe indicar:

- cuál lenguaje obtuvo el menor tiempo;
- cómo cambió la diferencia al aumentar n;
- si ambos produjeron resultados numéricos equivalentes;
- por qué existe una diferencia aunque ambos algoritmos sean O(n).

No se debe afirmar que C siempre es más rápido que Python en cualquier situación. La conclusión corresponde únicamente a las condiciones de este experimento.

## 13. Punto importante para la sustentación

En clase se puede hablar de Python como lenguaje interpretado frente a C como lenguaje compilado. Técnicamente, CPython primero convierte el código a bytecode y después lo ejecuta mediante su máquina virtual. Por eso, "interpretado" es una simplificación útil para el experimento, no significa que el procesador ejecute directamente cada línea del código fuente.
