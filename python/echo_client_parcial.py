import socket

SOCK_BUFFER = 4


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("192.168.0.55", 5500)

    print(f"Conectando al servidor en {server_address[0]}:{server_address[1]}")

    sock.connect(server_address)

    msg = "Hola mundo!"
    sock.sendall(msg.encode("utf-8"))
    data_str = ""

    cantidad_recibida = 0
    cantidad_esperada = len(msg.encode("utf-8"))

    while cantidad_recibida < cantidad_esperada:
        data = sock.recv(SOCK_BUFFER)
        cantidad_recibida += len(data)
        print(f"Recibi parcialmente: {data}")
        data_str += data.decode("utf-8")

    sock.close()

    print(f"Recibido: {data_str}")
