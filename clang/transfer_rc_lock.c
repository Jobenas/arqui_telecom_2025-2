#include <stdio.h>
#include <time.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>


#define NUM_THREADS 10
#define OPERATIONS_PER_THREAD 1000

typedef struct {
    int balance;
    int total_deposits;
    int total_withdrawals;
    pthread_mutex_t lock;
} BankAccount;

typedef struct {
    BankAccount* account;
    int thread_id;
} ThreadArgs;


void deposit(BankAccount* account, int amount) {
    pthread_mutex_lock(&account->lock);

    int temp = account->balance;
    // usleep(1);
    account->balance = temp + amount;
    account->total_deposits++;

    pthread_mutex_unlock(&account->lock);
}

void withdraw(BankAccount* account, int amount) {
    pthread_mutex_lock(&account->lock);

    int temp = account->balance;
    // usleep(1);
    if(temp >= temp) {
        account->balance = temp - amount;
        account->total_withdrawals++;
    }

    pthread_mutex_unlock(&account->lock);
}


void* realizar_transacciones(void* arg) {
    ThreadArgs* args = (ThreadArgs*)arg;
    BankAccount* account = args->account;
    int id = args->thread_id;

    printf("[Thread %d] Iniciando transacciones\n", id);

    for(int i=0; i < OPERATIONS_PER_THREAD; i++) {
        if(i % 2 == 0) {
            deposit(account, 10);
        } else {
            withdraw(account, 5);
        }
    }

    printf("[Thread %d] Transacciones completadas\n", id);

    return NULL;
}


int main(void) {
    BankAccount account;
    account.balance = 1000;
    account.total_deposits = 0;
    account.total_withdrawals = 0;
    
    pthread_mutex_init(&account.lock, NULL);
    
    pthread_t threads[NUM_THREADS];
    ThreadArgs args[NUM_THREADS];

    printf("Balance inicial: $%d\n", account.balance);
    printf("Operaciones por thread: %d\n", OPERATIONS_PER_THREAD);
    printf("Total de threads: %d\n", NUM_THREADS);

    clock_t inicio = clock();

    for(int i=0; i<NUM_THREADS; i++) {
        args[i].account = &account;
        args[i].thread_id = i;
        pthread_create(&threads[i], NULL, realizar_transacciones, &args[i]);
    }

    for(int i=0; i<NUM_THREADS; i++) {
        pthread_join(threads[i], NULL);
    }

    clock_t fin = clock();

    double t_ejecucion = (double)(fin - inicio) / CLOCKS_PER_SEC;

    int depositos_esperados = NUM_THREADS * (OPERATIONS_PER_THREAD / 2) * 10;
    int retiros_esperados = NUM_THREADS * (OPERATIONS_PER_THREAD / 2) * 5;
    int balance_esperado = 1000 + depositos_esperados - retiros_esperados;

    printf("balance final: %d\n", account.balance);
    printf("balance esperado: %d\n", balance_esperado);
    printf("Depositos registrados: %d - esperados: %d\n", account.total_deposits, NUM_THREADS * (OPERATIONS_PER_THREAD / 2));
    printf("Retiros registrados: %d - esperados: %d\n", account.total_withdrawals, NUM_THREADS * (OPERATIONS_PER_THREAD / 2));
    printf("Diferencia: %d\n", account.balance - balance_esperado);
    printf("Tiempo de ejecucion: %.6f segundos\n", t_ejecucion);
}