from flask import Blueprint, jsonify
import pandas as pd
import os

# traer modelo movieModel
from models.movieModel import MovieModel

main = Blueprint('movie_blueprint', __name__)

@main.route('/')
def get_home():
    try:
        movies = MovieModel.get_movie()
        
        movies_json = [movie.create_json() for movie in movies]
        
        return jsonify(movies_json), 200
    
    except Exception as e:
        
        return jsonify({'status': False, 'excepcion': str(e)}), 500

@main.route('/upload', methods=['POST'])
def post_movies():
    try:
        # Define la ruta completa al archivo CSV
        csv_file_path = os.path.join(os.path.dirname(__file__), '..', 'utils', 'peliculas.csv')
        
        # Lee el archivo CSV usando pandas
        movies = pd.read_csv(csv_file_path)

        #print(movies)

        # convertir el dataFrame en un diccionario

        movie_l = movies.to_dict(orient='records')
        
        # llamar al modelo
        
        req = MovieModel.post_movie(movie_l)

        return jsonify({'success': True, 'data':movie_l}), 200
                
    except Exception as e:
        
        return jsonify({'status': False, 'excepcion': str(e)}), 500
