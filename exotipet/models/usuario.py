# models/usuario.py
from models import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    tipo_id = db.Column(db.Integer, db.ForeignKey('tipo_usuario.id'))
