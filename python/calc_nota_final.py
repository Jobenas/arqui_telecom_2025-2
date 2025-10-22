import sys
import time


def busca_fila(codigo: str) -> str:
    """
    Busca una fila correspondiente a las notas, referidas por codigo de alumno en el archivo 'notas.csv'
    """
    try:
        with open("notas.csv", "r") as f:
            contenido = f.read()
    except FileNotFoundError:
        print("Archivo no existe")
        return ""
    tabla = contenido.split("\n")

    for idx in range(1, len(tabla)):
        fila = tabla[idx]
        if codigo in fila:
            return fila
    
    return ""     


def calc_nota_final(labs: list[int], e1: int, e2: int) -> float:
    """
    Calcula nota final a partir de las notas parciales de labs y examenes
    """
    prom_lab = sum(labs) / len(labs)

    nota_final = ((prom_lab * 5) + (e1 * 2.5) + (e2 * 2.5)) / 10

    return nota_final



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Se necesita ingresar el codigo de alumno")
        exit(1)
    
    inicio_io = time.perf_counter()
    with open("notas.csv", "r") as f:
        contenido = f.read()
    fin_io = time.perf_counter()


    inicio_proceso = time.perf_counter()
    tabla = contenido.split("\n")

    codigo = sys.argv[1]
    print(f"Codigo a buscar: {codigo}")
    fila = busca_fila(codigo)
    if not codigo:
        print("Codigo de alumno no existe en la base de datos")
        exit(1)
    
    fila = fila.split(",")

    labs = [int(fila[i]) for i in range(1, 13)]
    e1 = int(fila[13])
    e2 = int(fila[14])

    nota_final = calc_nota_final(labs, e1, e2)
    fin_proceso = time.perf_counter()

    print(f"La nota final del alumno con codigo {codigo}, es {nota_final:.2f}")

    print(f"El tiempo de I/O: {(fin_io - inicio_io):.6f} segundos")
    print(f"El tiempo de procesamiento: {(fin_proceso - inicio_proceso):.6f} segundos")
