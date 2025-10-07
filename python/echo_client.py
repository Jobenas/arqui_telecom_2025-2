import socket

SOCK_BUFFER = 1024


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("192.168.0.55", 5500)

    print(f"Conectando al servidor en {server_address[0]}:{server_address[1]}")

    sock.connect(server_address)

    msg = "Hola mundo!"
    sock.sendall(msg.encode("utf-8"))
    data = sock.recv(SOCK_BUFFER)

    data_str = data.decode("utf-8")

    print(f"Recibido: {data_str}")

    sock.close()
