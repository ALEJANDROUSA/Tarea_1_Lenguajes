import sys
import time


def calcular_suma(n):
    """Calcula la suma de la serie armónica hasta n."""
    suma = 0.0

    for i in range(1, n + 1):
        suma += 1.0 / i

    return suma


def main():
    if len(sys.argv) != 2:
        print(f"Uso: python {sys.argv[0]} <n>")
        sys.exit(1)

    n = int(sys.argv[1])

    if n <= 0:
        print("El valor de n debe ser mayor que cero.")
        sys.exit(1)

    inicio = time.perf_counter()

    resultado = calcular_suma(n)

    fin = time.perf_counter()

    tiempo = fin - inicio

    print(f"{resultado:.12f} {tiempo:.9f}")


if __name__ == "__main__":
    main()
