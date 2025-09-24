import json
import time

import requests


KEY = "ebb6989f"
url_base = "http://www.omdbapi.com"

cache = dict()

def busca_pelicula(titulo: str) -> dict | None:
    """
    Busca una pelicula por titulo, retorna un diccionario con los contenidos de la pelicula. Usa una caché
    :@param titulo: string que contiene el titulo de la pelicula
    :returns: dict con el formato entregado por omdb
    """
    info = cache.get(titulo, None)
    
    if not info:
        url = f"{url_base}/?t={movie}&apikey={KEY}"
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Codigo de estado: {response.status_code}")
            return None

        info = json.loads(response.text)

        cache[titulo] = info

    return info


def busca_rating(ratings: list[dict[str,str]], fuente: str) -> str:
    """
    Busca el rating correspondiente a la fuente señalada
    :@param ratings: lista de diccionarios con los ratings disponibles para el titulo
    :@param fuente: string con el nombre de la fuente de ratings que queremos usar
    :returns: string con el valor del rating especificado
    """

    for rating in ratings:
        if fuente == rating["Source"]:
            return rating["Value"]
    
    return "Rating No Disponible"


if __name__ == '__main__':

    with open("cache_peliculas", "r") as f:
        data = f.read()
        print(f"data: {data}")
        if len(data) > 0:
            cache = json.loads(data)
    
    while (True):
        movie = input("Indique el nombre de la pelicula o serie que quiere revisar / presione q (Q) para terminar: ")

        if movie.lower() == "q":
            print("Terminando programa")
            with open("cache_peliculas", "w+") as f:
                f.write(json.dumps(cache))
            exit(0)

        inicio = time.perf_counter()
        data = busca_pelicula(movie)
        fin = time.perf_counter()

        if not data:
            print("No se encontró el titulo")
            continue
        
        print(f"Titulo: {data['Title']}, Fecha de Estreno: {data['Released']}, Director: {data['Director'] if data['Director'] != "N/A" else "No Disponible"}, Puntaje: {busca_rating(data['Ratings'], "Rotten Tomatoes")}")
        print(f"Tiempo total de busqueda: {(fin - inicio):.6f} Segundos")