import sys
import time


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
    encontre = False
    for idx in range(1, len(tabla)):
        fila = tabla[idx].split(",")
        if codigo == fila[0]:
            labs = [int(fila[i]) for i in range(1, 13)]
            e1 = int(fila[13])
            e2 = int(fila[14])
            encontre = True
            break
    
    if not encontre:
        print("Codigo de alumno no existe en la base de datos")
        exit(1)
    
    prom_lab = sum(labs) / len(labs)

    nota_final = ((prom_lab * 5) + (e1 * 2.5) + (e2 * 2.5)) / 10
    fin_proceso = time.perf_counter()

    print(f"La nota final del alumno con codigo {codigo}, es {nota_final:.2f}")

    print(f"El tiempo de I/O: {(fin_io - inicio_io):.6f} segundos")
    print(f"El tiempo de procesamiento: {(fin_proceso - inicio_proceso):.6f} segundos")
