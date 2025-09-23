#include <stdio.h>
#include <stdint.h>
#include <stddef.h>


static long promedio(long a, long b, long c) {
    long tmp1 = a + b;
    long tmp2 = tmp1 + c;
    long avg = tmp2 / 3;

    return avg;
}


long suma_y_promedio(const int *arr, size_t n, long *out_avg) {
    long suma = 0;
    
    for(int i=0; i<n; i++) {
        suma += arr[i];
    }

    long avg = promedio(suma, (long)n, (long)(n>0));

    if(out_avg) {
        *out_avg = avg;
    }

    return suma;
}


int main(void) {
    int datos[5] = {10, 20, 30, 40, 50};
    long avg = -1;
    long s  = suma_y_promedio(datos, 5, &avg);
    printf("Suma=%ld, promedio=%ld\n", s, avg);

    return 0;
}
