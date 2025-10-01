#include <stdio.h>


#define ROWS 3
#define COLS 4

int main(void) {
    int matrix[ROWS][COLS];
    int counter = 1;

    for (int i = 0; i < ROWS; i++) {
        for(int j = 0; j < COLS; j++) {
            matrix[i][j] = counter++;
        }
    }

    printf("Contenidos de la matriz (fila x columna): \n");

    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            printf("%3d ", matrix[i][j]);
        }
        printf("\n");
    }

    // recorrido Row-major: el loop interno es para las columnas
    printf("Recorrido Row-Major:\n");

    int suma = 0;
    for(int i=0; i<ROWS; i++){
        for(int j=0; j<COLS; j++) {
            int value = matrix[i][j];
            printf("Accediendo elemento [%d][%d] = %d (direccion %p)\n", i, j, value, (void*)&matrix[i][j]);
            suma += value;
        }
    }

    printf("\nSuma final (row-major): %d\n", suma);

    return 0;
}
