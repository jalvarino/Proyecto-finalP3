from Flask import Flask
from flask_cors import CORS
from .database import init_db

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'tu_contraseña'
    app.config['MYSQL_DB'] = 'servicio_social'

    init_db(app)

    from .routes import main
    app.register_blueprint(main)

    return app
