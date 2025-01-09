from flask import Flask
from config import config
#routes
from routes import home


app=Flask(__name__)

def not_found(error):
    return "<h1>Pagina no encontrado</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['dev'])

    #blueprints o mapas de rutas
    #cuando acceda a localhost:5000/api/home entonces ejecutara:
    app.register_blueprint(home.main, url_prefix='/api/home')

    # manejar error
    app.register_error_handler(404, not_found)

    app.run()