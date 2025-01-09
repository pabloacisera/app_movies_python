from database.conn import get_connect
from .entities.movie import MovieEntity

class MovieModel:
    # Obtener todas las películas
    @classmethod
    def get_movie(cls):
        try:
            conn = get_connect()
            movies = []

            with conn.cursor() as cursor:
                cursor.execute('SELECT * FROM movies ORDER BY titulo ASC')
                results = cursor.fetchall()

                for row in results:
                    movie = MovieEntity(*row)  # Crea una entidad MovieEntity con los datos
                    movies.append(movie)

            conn.close()
            return movies
        except Exception as e:
            raise Exception(f"Error al obtener películas: {e}")

    # Agregar películas a la base de datos
    @classmethod
    def post_movie(cls, data):
        try:
            conn = get_connect()
            with conn.cursor() as cursor:
                for movie in data:
                    query = """
                        INSERT INTO movies(
                            titulo, descripcion, duracion, estreno, poster, año,
                            categoria, idioma, genero, clasificacion, calificacion, popularidad
                        )
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    cursor.execute(query, (
                        movie['titulo'], movie['descripcion'], movie['duracion'], 
                        movie['estreno'], movie['poster'], movie['año'], 
                        movie['categoria'], movie['idioma'], movie['genero'], 
                        movie['clasificacion'], movie['calificacion'], movie['popularidad']
                    ))
                conn.commit()
            conn.close()
            return True
        except Exception as e:
            raise Exception(f"Error al insertar películas: {e}")
