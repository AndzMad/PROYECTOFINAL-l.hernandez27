from dotenv import load_dotenv  # Carga las variables de entorno definidas en .env
import os

load_dotenv(override=True)


class Config:
    # Se trae desde el dotenv las claves secretas "variables de entorno" para que no se vean
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
