class MovieEntity:
    # Constructor
    def __init__(self, id, create_time=None, titulo=None, descripcion=None, duracion=None, 
                 estreno=None, poster=None, año=None, categoria=None, idioma=None, 
                 genero=None, clasificacion=None, calificacion=None, popularidad=None):
        self.id = id
        self.create_time = create_time
        self.titulo = titulo
        self.descripcion = descripcion
        self.duracion = duracion
        self.estreno = estreno
        self.poster = poster
        self.año = año
        self.categoria = categoria
        self.idioma = idioma
        self.genero = genero
        self.clasificacion = clasificacion
        self.calificacion = calificacion
        self.popularidad = popularidad

    def create_json(self):
        return {
            'id': self.id,
            'create_time': self.create_time,
            'titulo': self.titulo,
            'descripcion': self.descripcion,
            'duracion': self.duracion,
            'estreno': self.estreno,
            'poster': self.poster,
            'año': self.año,
            'categoria': self.categoria,
            'idioma': self.idioma,
            'genero': self.genero,
            'clasificacion': self.clasificacion,
            'calificacion': self.calificacion,
            'popularidad': self.popularidad
        }



		