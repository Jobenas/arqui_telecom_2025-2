import ctypes as C
import time
import math

try:
    import numpy as np
    use_numpy = True
except ImportError:
    use_numpy = False

lib = C.CDLL("./librowcol.so")
lib.sum_row_major.argtypes = [C.POINTER(C.c_double), C.c_size_t, C.c_size_t]
lib.sum_row_major.restype = C.c_double
lib.sum_col_major.argtypes = [C.POINTER(C.c_double), C.c_size_t, C.c_size_t]
lib.sum_col_major.restype = C.c_double

def make_matrix(rows, cols, fill=1.0):
    n = rows * cols

    if use_numpy:
        a = np.full((rows, cols), fill, dtype=np.float64, order="C")
        return a, a.ctypes.data_as(C.POINTER(C.c_double))
    else:
        buf = (C.c_double *n)()
        for i in range(n):
            buf[i] = fill
        return buf, C.cast(buf, C.POINTER(C.c_double))

def time_it(fn, *args, repeats=3, warmup=1):
    for _ in range(warmup):
        fn(*args)
    best = math.inf
    for _ in range(repeats):
        t0 = time.perf_counter()
        res = fn(*args)
        t1 = time.perf_counter()
        best = min(best, t1-t0)
    return best, res


if __name__ == '__main__':
    rows, cols = 4096, 2048

    mat, ptr = make_matrix(rows, cols, 1.0)

    t_row, sum_row = time_it(lib.sum_row_major, ptr, rows, cols)
    t_col, sum_col = time_it(lib.sum_col_major, ptr, rows, cols)

    print(f"rows={rows}, cols={cols}")
    print(f"sum_row_major: {sum_row:0.1f}, tiempo={t_row*1000:.2f} ms")
    print(f"sum_col_major: {sum_col:0.1f}, tiempo={t_col*1000:.2f} ms")
    print(f"speedup (row/col): {t_col/t_row:.2f} mas rapido")

