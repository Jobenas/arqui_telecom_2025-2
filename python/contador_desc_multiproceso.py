from multiprocessing import Process
import time

N = 100_000_000


def countdown(n: int):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    inicio = time.perf_counter()
    p1 = Process(target=countdown, args=(N // 2, ))
    p2 = Process(target=countdown, args=(N // 2, ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    fin = time.perf_counter()

    t_ejecucion = fin - inicio

    print(f"Tiempo de ejecución multiproceso: {t_ejecucion:.6f} segundos")
