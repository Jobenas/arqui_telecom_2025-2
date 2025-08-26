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


def realiza_operacion(resultados: list[int | float], operacion) -> float:
    match operacion:
        case "promedio":
            resultado = sum(resultados) / len(resultados)
        case "mediana":
            resultados.sort()
            resultado = resultados[len(resultados) // 2]
        case _:
            print("operacion seleccionada es invalida, terminando.")
            exit(2)

    return resultado



def evalua_funcion(func, usa_idx: bool, numeros: list[int], indice: int, operacion: str, iteraciones: int) -> float:
    l = list()

    for _ in range(iteraciones):
        inicio = time.perf_counter()
        promedio = func(numeros, indice) if usa_idx else func(numeros)
        fin = time.perf_counter()
        l.append(fin - inicio)

    resultado = realiza_operacion(l, operacion)

    return resultado


if __name__ == '__main__':
    NUM_MUESTRAS = 10
    lista = list()
    fin = False
    idx = 0

    arg_num = len(sys.argv)

    if arg_num <= 2:
        print("Se necesitan pasar argumentos")
        exit(1)
    
    for i in range(2, arg_num):
        lista.append(int(sys.argv[i]))
    
    idx = arg_num - 2

    tp1 = evalua_funcion(promedio_opcion1, True, lista, idx, sys.argv[1], NUM_MUESTRAS)
    tp2 = evalua_funcion(promedio_opcion2, False, lista, None, sys.argv[1], NUM_MUESTRAS)
    tp3 = evalua_funcion(promedio_opcion3, False, lista, None, sys.argv[1], NUM_MUESTRAS)
    tp4 = evalua_funcion(promedio_opcion4, False, lista, None, sys.argv[1], NUM_MUESTRAS)

    print(f"Resultados: opcion1 -> {(tp1)} segundos | opcion2 -> {(tp2)} segundos | opcion3 -> {(tp3)} segundos | opcion4 -> {(tp4)} segundos")

    print("Fin del programa")

