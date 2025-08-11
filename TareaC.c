#include <stdio.h>
#include <time.h>

unsigned long long facto_r(int n) {
    if (n == 0 || n == 1)
        return 1;
    else
        return n * facto_r(n - 1);
}

unsigned long long facto_i(int n) {
    unsigned long long resultado = 1;
    for (int i = 2; i <= n; i++) {
        resultado *= i;
    }
    return resultado;
}

int main() {
    int n;
    printf("Ingresa el valor de n: ");
    scanf("%d", &n);

    // Medir tiempo recursivo
    clock_t inicio = clock();
    unsigned long long resultado_r = facto_r(n);
    clock_t fin = clock();
    double tiempo_r = ((double)(fin - inicio)) / CLOCKS_PER_SEC;

    // Medir tiempo iterativo
    inicio = clock();
    unsigned long long resultado_i = facto_i(n);
    fin = clock();
    double tiempo_i = ((double)(fin - inicio)) / CLOCKS_PER_SEC;

    printf("\nRecursivo: %d! = %llu, Tiempo: %f segundos\n", n, resultado_r, tiempo_r);
    printf("Iterativo: %d! = %llu, Tiempo: %f segundos\n", n, resultado_i, tiempo_i);

    return 0;
}

