#include <stdio.h>
#include <stdlib.h>

#define API

API float promedio(int *buf, size_t n) {
    int suma = 0;
    int cuenta = 0;

    for (int i= 0; i < n; i++) {
        int num = *(buf + i);
        printf("Numero a sumar: %d\r\n", num);
        suma += num;
    }

    printf("resultado de la suma: %d\r\n", suma);

    if (n == 0) {
        printf("No se pasaron numeros a promediar");
        return -1;
    }

    float prom = (float)suma / (float)n;
    
    printf("Promedio de %d numeros: %.6f\r\n", n, prom);
    return prom;
}


int main(int argc, char *argv[]) {

    if (argc < 2) {
        printf("Se necesitan pasar todos los argumentos\r\n");
        return 1;
    }
    int count = argc - 1;
    int *arrDinamico;     // Puntero para el arreglo creado dinamicamente

    arrDinamico = (int *)malloc(count * sizeof(int));

    if (arrDinamico == NULL) {
        printf("Fallo en reserva de memoria");
        return 2;
    }

    for (int i = 0; i < count; i++) {
        arrDinamico[i] = atoi(argv[i + 1]);
    }
    
    float p = promedio(arrDinamico, count);
    free(arrDinamico);

    printf("Promedio de %d numeros: %.6f\r\n", count, p);
    return 0;
}
