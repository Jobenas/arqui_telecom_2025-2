#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

float promedio(int *buf, size_t n) {
    int suma = 0;
    int cuenta = 0;

    for (int i= 0; i < n; i++) {
        int num = *(buf + i);
        suma += num;
    }

    if (n == 0) {
        printf("No se pasaron numeros a promediar");
        return -1;
    }

    float prom = (float)suma / (float)n;
    
    return prom;
}