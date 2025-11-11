import time

N = 1_000_000


def countdown(n: int):
    while n > 0:
        n -= 1


if __name__ == "__main__":
    inicio = time.perf_counter()
    countdown(N)
    fin = time.perf_counter()

    t_ejecucion = fin - inicio

    print(f"Tiempo de ejecución: {t_ejecucion:.6f} segundos")
