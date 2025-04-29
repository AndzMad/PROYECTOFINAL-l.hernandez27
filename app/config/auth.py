from flask_login import LoginManager
from app.config.db import Usuario


"""
    Parte 1 - Punto 2 | Tabla Usuarios
    Implemente también un método que permita consultar en la tabla si un usuario y contraseña coinciden,
"""

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id: str) -> Usuario:

    try:
        user = Usuario.query.get(str(user_id))
        print("Ok user")
        return user
    except Exception as e:
        print(f"Error al cargar el usuario: {e}")
        return None
