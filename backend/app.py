from flask import Flask
from flask_cors import CORS
from models import db
from routes import bp as routes_bp
from commands import init_db_command

# Inicialización de Flask
app = Flask(__name__)
CORS(app)  # Habilitar solicitudes desde el frontend
app.config.from_object('config.Config')

# Conexión a la base de datos
db.init_app(app)

# Registro de rutas
app.register_blueprint(routes_bp)

# Registro de comandos
app.cli.add_command(init_db_command)

if __name__ == '__main__':
    app.run(debug=True)
