import socket
import time

SOCK_BUFFER = 1024
notas_num = 200
codigo_inicial = 20250001

def calc_nota_final(labs: list[int], e1: int, e2: int) -> float:
    """
    Calcula nota final a partir de las notas parciales de labs y examenes
    """
    prom_lab = sum(labs) / len(labs)

    nota_final = ((prom_lab * 5) + (e1 * 2.5) + (e2 * 2.5)) / 10

    return nota_final    


def obten_notas_parciales(codigo: str) -> list[int]:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 5000)

    # print(f"Conectando al servidor en {server_address[0]}:{server_address[1]}")

    sock.connect(server_address)

    sock.sendall(codigo.encode("utf-8"))

    data = sock.recv(SOCK_BUFFER)

    data_str = data.decode("utf-8")
    notas = data_str.split(",")
    return [int(notas[i]) for i in range(1, len(notas))]


if __name__ == '__main__':
    inicio = time.perf_counter() 
    notas_finales = list()

    for i in range(200):
        codigo = codigo_inicial + i
        notas_parciales = obten_notas_parciales(f"{codigo}")
        nota_final = calc_nota_final(notas_parciales[:12], notas_parciales[12], notas_parciales[13])
        notas_finales.append(nota_final)

    nota_final_promedio = sum(notas_finales) / len(notas_finales)
    fin = time.perf_counter()

    t_ejecucion = fin - inicio

    print(f"El promedio de notas finales es: {nota_final_promedio}")
    print(f"Tiempo total de ejecucion: {t_ejecucion:.6f} segundos")
    print("fin del programa")