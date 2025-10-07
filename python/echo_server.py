import socket

SOCK_BUFFER = 1024


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("0.0.0.0", 5500)

    print(f"Iniciando el servidor en {server_address[0]}:{server_address[1]}")

    sock.bind(server_address)

    sock.listen(1)

    while True:
        print("Esperando conexiones...")

        conn, addr = sock.accept()

        print(f"Conexión establecida desde {addr[0]}:{addr[1]}")

        try:
            while True:
                data = conn.recv(SOCK_BUFFER)
                if data:
                    print(f"Recibido: {data.decode('utf-8')}")
                    conn.sendall(data)
                else:
                    print("No hay mas datos.")
                    break
        except ConnectionResetError:
            print("El cliente cerró la conexión abruptamente.")
        finally:
            print("Cerrando la conexión.")
            conn.close()
