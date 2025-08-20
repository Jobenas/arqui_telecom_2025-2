import time


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
    lista = list()
    fin = False
    idx = 0

    while not fin:
        numero = input("Ingrese un numero: ")
        if numero == "q":
            fin = True
        else:
            numero = int(numero)
            lista.append(numero)
            idx += 1

    inicio1 = time.perf_counter()
    promedio = promedio_opcion1(lista, idx)
    fin1 = time.perf_counter()
    print(f"Promedio calculado: {promedio}")

    inicio2 = time.perf_counter()
    promedio = promedio_opcion2(lista)
    fin2 = time.perf_counter()
    print(f"Promedio calculado: {promedio}")

    inicio3 = time.perf_counter()
    promedio = promedio_opcion3(lista)
    fin3 = time.perf_counter()
    print(f"Promedio calculado: {promedio}")

    inicio4 = time.perf_counter()
    promedio = promedio_opcion4(lista)
    fin4 = time.perf_counter()
    print(f"Promedio calculado: {promedio}")

    print(f"Resultados: opcion1 -> {(fin1 - inicio1)} segundos | opcion2 -> {(fin2 - inicio2)} segundos | opcion3 -> {(fin3 - inicio3)} segundos | opcion4 -> {(fin4 - inicio4)} segundos")

    print("Fin del programa")

