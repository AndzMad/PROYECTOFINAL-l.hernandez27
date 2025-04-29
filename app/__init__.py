from flask import Flask
from app.config.db import db, crear_usuarios
from app.config.auth import login_manager
from app.config.routes import registrar_rutas
from app.services.cargador_heladeria import cargar_modulos_desde_BD

def create_app(config) -> Flask:
    
    app = Flask(__name__, template_folder='views') # Se instancia la app
    app.config.from_object(config) # Recibe las variables de entorno.
    db.init_app(app) # Inicializa SQLAlchemy con la configuración de esa app.
    login_manager.init_app(app) # Asocia la app a la instancia de LoginManager
    
    
    registrar_rutas(app) # Registra la Blueprint en el app
    
    with app.app_context():
        db.create_all() # Crea todas las tablas de los modelos registrados en la base de datos, si no existen.
        app.config['heladeria'] = cargar_modulos_desde_BD()
        crear_usuarios() # Llama la función que crea los usuarios.
    
    return app