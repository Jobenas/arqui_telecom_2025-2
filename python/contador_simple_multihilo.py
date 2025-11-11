import time
from threading import Thread


def cuenta(idx: int):
    print(f"[{idx}] Uno")
    time.sleep(1)
    print(f"[{idx}] Dos")


def main():
    t1 = Thread(target=cuenta, args=(1, ))
    t2 = Thread(target=cuenta, args=(2, ))
    t3 = Thread(target=cuenta, args=(3, ))

    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()


if __name__ == '__main__':
    inicio = time.perf_counter()
    main()
    fin = time.perf_counter() 

    t_ejecucion = fin - inicio

    print(f"Tiempo de ejecución: {t_ejecucion:.6f} segundos")

