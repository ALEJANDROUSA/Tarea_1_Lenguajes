import csv
from pathlib import Path

import matplotlib.pyplot as plt


BASE = Path(__file__).resolve().parent.parent
ARCHIVO_RESULTADOS = BASE / "resultados" / "resultados.csv"
ARCHIVO_GRAFICA = Path(__file__).resolve().parent / "comparacion_rendimiento.png"

n = []
tiempos_c = []
tiempos_python = []

with open(ARCHIVO_RESULTADOS, "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        n.append(int(fila["n"]))
        tiempos_c.append(float(fila["tiempo_c_segundos"]))
        tiempos_python.append(float(fila["tiempo_python_segundos"]))

plt.figure(figsize=(9, 6))

plt.plot(n, tiempos_c, marker="o", label="C")
plt.plot(n, tiempos_python, marker="o", label="Python")

plt.xlabel("Cantidad de términos (n)")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.title("Rendimiento de la suma de una serie: C vs Python")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(ARCHIVO_GRAFICA, dpi=300)
plt.show()

print(f"Gráfica guardada en: {ARCHIVO_GRAFICA}")
