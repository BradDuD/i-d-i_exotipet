from flask import Flask
from config import Config
from models import db
from models.usuario import Usuario
from models.tipousuario import TipoUsuario
from routes import main,login

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(main)


# Crear las tablas en la base de datos
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
