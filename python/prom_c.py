import os
import ctypes as C


# 3) Crear funcion que construcya el arreglo en C una sola vez 
def to_c_array_int(nums: list[int]):
    arr_t = C.c_int16 * len(nums)
    arr = arr_t(*nums)
    n = C.c_size_t(len(nums))

    return arr, n


if __name__ == '__main__':
    # 1) Cargar la libreria
    # lib = C.CDLL(os.path.abspath("../clang/libprom.so"))
    lib = C.CDLL("./libprom.so")

    # 2) Declarar todos los elementos de lenguaje C
    lib.promedio.argtypes = [C.POINTER(C.c_int16), C.c_size_t]
    lib.promedio.restype = C.c_float

    # 4) Llama a la funcion y a la libreria
    numeros = [12, 13, 14, 15, 16, 17, 18]    
    arreglo, cuenta = to_c_array_int(numeros)

    prom = lib.promedio(arreglo, cuenta)

    print(f"Resultado del promedio: {prom}")
