#include <stdio.h>
#include <time.h>
#include <pthread.h>

#define N 1000000

void* countdown(void* arg) {
    int n = *(int*)arg;
    while (n > 0) {
        n--;
    }

    return NULL;
}


int main() {
    pthread_t t1, t2;
    int n1 = N / 2;
    int n2 = N / 2;

    clock_t inicio = clock();
    pthread_create(&t1, NULL, countdown, &n1);
    pthread_create(&t2, NULL, countdown, &n2);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    
    clock_t fin = clock();

    double t_ejecucion = (double)(fin - inicio) / CLOCKS_PER_SEC;

    printf("Tiempo de ejecucion (multihilo): %.6f segundos\r\n", t_ejecucion);

    return 0;
}
