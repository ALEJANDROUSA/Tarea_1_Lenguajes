#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/*
 * Calcula la suma:
 *
 * S = 1 + 1/2 + 1/3 + ... + 1/n
 */
double calcular_suma(long long n) {
    double suma = 0.0;

    for (long long i = 1; i <= n; i++) {
        suma += 1.0 / (double)i;
    }

    return suma;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Uso: %s <n>\n", argv[0]);
        return 1;
    }

    long long n = atoll(argv[1]);

    if (n <= 0) {
        printf("El valor de n debe ser mayor que cero.\n");
        return 1;
    }

    clock_t inicio = clock();

    double resultado = calcular_suma(n);

    clock_t fin = clock();

    double tiempo = (double)(fin - inicio) / CLOCKS_PER_SEC;

    printf("%.12f %.9f\n", resultado, tiempo);

    return 0;
}
