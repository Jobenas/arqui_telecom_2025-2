import ctypes as C
import os
import sys


# 3) Crear funcion que construcya el arreglo en C una sola vez 
def to_c_array_int(nums: list[int]):
    arr_t = C.c_int * len(nums)
    arr = arr_t(*nums)
    n = C.c_size_t(len(nums))

    return arr, n


if __name__ == '__main__':
    arg_num = len(sys.argv)

    numeros = list()

    for i in range(1, arg_num):
        numeros.append(int(sys.argv[i]))

    if arg_num < 2:
        print("Se necesitan pasar argumentos")
        exit(1)

    # 1) Cargar la libreria
    # lib = C.CDLL(os.path.abspath("../clang/libprom.so"))
    lib = C.CDLL("./libprom.so")

    # 2) Declarar todos los elementos de lenguaje C
    lib.promedio.argtypes = [C.POINTER(C.c_int), C.c_size_t]
    lib.promedio.restype = C.c_float

    # 4) Llama a la funcion y a la libreria
    arreglo, cuenta = to_c_array_int(numeros)

    prom = lib.promedio(arreglo, cuenta)

    print(f"Resultado del promedio: {prom}")
