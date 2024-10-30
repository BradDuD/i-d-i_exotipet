import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave_secreta_de_prueba'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/veterinaria'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
