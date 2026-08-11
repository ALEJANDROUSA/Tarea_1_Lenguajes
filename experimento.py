import csv
import platform
import subprocess
import sys
from pathlib import Path


TAMANOS = [1_000_000, 2_000_000, 5_000_000, 10_000_000, 20_000_000]
REPETICIONES = 3

BASE = Path(__file__).resolve().parent.parent
SRC = BASE / "src"
RESULTADOS = BASE / "resultados"

ARCHIVO_C = SRC / "suma_armonica.c"
ARCHIVO_PYTHON = SRC / "suma_armonica.py"

if platform.system() == "Windows":
    EJECUTABLE_C = SRC / "suma_armonica.exe"
else:
    EJECUTABLE_C = SRC / "suma_armonica"


def compilar_c():
    comando = [
        "gcc", "-O2", str(ARCHIVO_C), "-o", str(EJECUTABLE_C)
    ]
    subprocess.run(comando, check=True)


def ejecutar_c(n):
    proceso = subprocess.run(
        [str(EJECUTABLE_C), str(n)],
        capture_output=True,
        text=True,
        check=True
    )

    resultado, tiempo = proceso.stdout.strip().split()
    return float(resultado), float(tiempo)


def ejecutar_python(n):
    proceso = subprocess.run(
        [sys.executable, str(ARCHIVO_PYTHON), str(n)],
        capture_output=True,
        text=True,
        check=True
    )

    resultado, tiempo = proceso.stdout.strip().split()
    return float(resultado), float(tiempo)


def medir(funcion, n):
    tiempos = []
    resultados = []

    for _ in range(REPETICIONES):
        resultado, tiempo = funcion(n)
        resultados.append(resultado)
        tiempos.append(tiempo)

    promedio = sum(tiempos) / len(tiempos)
    return resultados[-1], promedio


def main():
    RESULTADOS.mkdir(exist_ok=True)

    print("Compilando C...")
    compilar_c()

    filas = []

    print("\nINICIO DEL EXPERIMENTO")
    print("-" * 55)

    for n in TAMANOS:
        print(f"\nn = {n:,}")

        resultado_c, tiempo_c = medir(ejecutar_c, n)
        resultado_python, tiempo_python = medir(ejecutar_python, n)

        factor = tiempo_python / tiempo_c if tiempo_c > 0 else 0
        diferencia = abs(resultado_c - resultado_python)

        print(f"C      : {tiempo_c:.6f} s")
        print(f"Python : {tiempo_python:.6f} s")
        print(f"Python/C: {factor:.2f} veces")
        print(f"Diferencia numérica: {diferencia:.12e}")

        filas.append([
            n, tiempo_c, tiempo_python, factor,
            resultado_c, resultado_python, diferencia
        ])

    archivo = RESULTADOS / "resultados.csv"

    with open(archivo, "w", newline="", encoding="utf-8") as salida:
        escritor = csv.writer(salida)
        escritor.writerow([
            "n",
            "tiempo_c_segundos",
            "tiempo_python_segundos",
            "factor_python_sobre_c",
            "resultado_c",
            "resultado_python",
            "diferencia_numerica"
        ])
        escritor.writerows(filas)

    print("\nExperimento terminado.")
    print(f"Resultados guardados en: {archivo}")


if __name__ == "__main__":
    main()
