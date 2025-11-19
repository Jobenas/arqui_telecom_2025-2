#include <stdio.h>
#include <time.h>

#define N 1000000


void countdown(int n) {
    while(n > 0) {
        n--;
    }
}

int main(void) {
       
    clock_t inicio = clock();

    countdown(N);

    clock_t fin = clock();

    double t_ejecucion = (double)(fin - inicio) / CLOCKS_PER_SEC;

    printf("Tiempo de ejecucion (secuencial): %.6f segundos\r\n", t_ejecucion);

    return 0;
}
