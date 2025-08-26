import time
import sys


def promedio_opcion1(numeros: list[int], indice: int) -> float:
    acumulado = 0
    for i in range(indice):
        acumulado += numeros[i]

    promedio = acumulado / indice

    return promedio


def promedio_opcion2(numeros: list[int]) -> float:
    acumulado = 0
    for i in range(len(numeros)):
        acumulado += numeros[i]

    promedio = acumulado / len(numeros)

    return promedio


def promedio_opcion3(numeros: list[int]) -> float:
    acumulado = 0

    for i in numeros:
        acumulado += i

    promedio = acumulado / len(numeros)

    return promedio


def promedio_opcion4(numeros: list[int]) -> float:
    promedio = sum(lista) / len(lista)

    return promedio


if __name__ == '__main__':
    NUM_MUESTRAS = 10
    lista = list()
    fin = False
    idx = 0

    arg_num = len(sys.argv)

    if arg_num <= 2:
        print("Se necesitan pasar argumentos")
        exit(1)
    
    operacion = sys.argv[1]

    for i in range(2, arg_num):
        lista.append(int(sys.argv[i]))
    
    idx = arg_num - 2

    tiempos_opcion1 = list()
    for _ in range(NUM_MUESTRAS):
        inicio = time.perf_counter()
        promedio = promedio_opcion1(lista, idx)
        fin = time.perf_counter()
        tiempos_opcion1.append(fin - inicio)

    tiempos_opcion2 = list()
    for _ in range(NUM_MUESTRAS):
        inicio = time.perf_counter()
        promedio = promedio_opcion2(lista)
        fin = time.perf_counter()
        tiempos_opcion2.append(fin - inicio)

    tiempos_opcion3 = list()
    for _ in range(NUM_MUESTRAS):
        inicio = time.perf_counter()
        promedio = promedio_opcion3(lista)
        fin = time.perf_counter()
        tiempos_opcion3.append(fin - inicio)

    tiempos_opcion4 = list()
    for _ in range(NUM_MUESTRAS):
        inicio = time.perf_counter()
        promedio = promedio_opcion4(lista)
        fin = time.perf_counter()
        tiempos_opcion4.append(fin - inicio)

    match operacion:
        case "promedio":
            tp1 = sum(tiempos_opcion1) / NUM_MUESTRAS
            tp2 = sum(tiempos_opcion2) / NUM_MUESTRAS
            tp3 = sum(tiempos_opcion3) / NUM_MUESTRAS
            tp4 = sum(tiempos_opcion4) / NUM_MUESTRAS
        case "mediana":
            tiempos_opcion1.sort()
            tiempos_opcion2.sort()
            tiempos_opcion3.sort()
            tiempos_opcion4.sort()

            tp1 = tiempos_opcion1[len(tiempos_opcion1) // 2]
            tp2 = tiempos_opcion2[len(tiempos_opcion2) // 2]
            tp3 = tiempos_opcion3[len(tiempos_opcion3) // 2]
            tp4 = tiempos_opcion4[len(tiempos_opcion4) // 2]
        case _:
            print("operacion seleccionada es invalida, terminando.")
            exit(2)

    print(f"Tiempos para opcion 1: {tiempos_opcion1}")

    print(f"Resultados: opcion1 -> {(tp1)} segundos | opcion2 -> {(tp2)} segundos | opcion3 -> {(tp3)} segundos | opcion4 -> {(tp4)} segundos")

    print("Fin del programa")

