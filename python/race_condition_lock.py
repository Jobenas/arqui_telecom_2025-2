from concurrent.futures import ThreadPoolExecutor
from threading import Lock
import time


class FakeDatabase:
    def __init__(self):
        self.value = 0
        self.lock = Lock()
    
    def update(self, name):
        print(f"[Thread {name}] Iniciando actualizacion")
        print(f"[Thread {name}] A punto de obtener el candado")
        with self.lock:
            print(f"[Thread {name}] Candado obtenido")
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            print(f"[Thread {name}] A punto de liberar el candado")
        print(f"[Thread {name}] Candado liberado")
        print(f"[Thread {name}] Ha finalizado la actualizacion")


if __name__ == '__main__':
    workers = 2
    tasks = workers

    db = FakeDatabase()
    print(f"Valor inicial de la base de datos: {db.value}")

    with ThreadPoolExecutor(max_workers=workers) as executor:
        for idx in range(tasks):
            executor.submit(db.update, idx)
        
    print(f"El valor final de la base de datos es: {db.value}")
