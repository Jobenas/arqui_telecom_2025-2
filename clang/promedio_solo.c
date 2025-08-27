#include <stdio.h>
#include <stdlib.h>


int main(int argc, char *argv[]) {

    if (argc < 2) {
        printf("Se necesitan pasar todos los argumentos\r\n");
        return 1;
    }

    long suma = 0;
    int count = 0;

    for (int i=0; i<argc; i++) {
        char *endPtr;
        long long val = strtoll(argv[i], &endPtr, 10);

        if(*endPtr != '\0') {
            printf("Caracter invalido\r\n");
            return 2;
        }

        suma += val;
        count++;
    }

    if (count == 0) {
        printf("No hay numeros para promediar\r\n");
        return 3;
    }

    double promedio = (double)suma / (double)count;
    printf("Promedio de %d numeros: %.6f\r\n", count, promedio);

    return 0;
}
