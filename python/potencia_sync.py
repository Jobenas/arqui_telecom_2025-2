import time


def calc_potencia(base: int, exp: int) -> int:
    potencia = 1

    while exp > 0:
        potencia *= base
        exp -= 1
    

    return potencia


if __name__ == '__main__':
    N = 200_000
    inicio = time.perf_counter()
    res = calc_potencia(N, N)
    fin = time.perf_counter()

    t_ejecucion = fin - inicio
    print(f"Tiempo total: {t_ejecucion:.6f} segundos")

