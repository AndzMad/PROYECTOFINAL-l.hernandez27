from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

# Crea una instancia vacía de SQLAlchemy en db, para importar dentro del create_app()
db = SQLAlchemy()

"""
    Parte 1 - Punto 2 | Tabla Usuarios
    Construya una clase usuario con los atributos id, username y password. 
    Adicionalmente construya una tabla con SQLAlchemy que tenga estas 3 columnas precisamente. 
"""
class Usuario(UserMixin, db.Model):

    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    es_admin = db.Column(db.Integer, nullable=False, default=False)
    es_empleado = db.Column(db.Integer, nullable=False, default=False)


class IngredientesDB(db.Model):

    __tablename__ = 'ingredientes'

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    calorias = db.Column(db.Integer, nullable=False)
    inventario = db.Column(db.Float, nullable=False)
    vegetariano = db.Column(db.Boolean, nullable=False)
    sabor = db.Column(db.String(50), nullable=True)


class ProductosDB(db.Model):

    __tablename__ = 'productos'

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)  # Copa o Malteada
    nombre = db.Column(db.String(50), nullable=False)
    id_ingrediente1 = db.Column(db.Integer, db.ForeignKey('ingredientes.id'))
    id_ingrediente2 = db.Column(db.Integer, db.ForeignKey('ingredientes.id'))
    id_ingrediente3 = db.Column(db.Integer, db.ForeignKey('ingredientes.id'))
    precio_publico = db.Column(db.Float, nullable=False)
    # Solo aplica para malteadas
    volumen = db.Column(db.Integer, nullable=True)
    # Solo aplica para copas
    tipo_vaso = db.Column(db.String(15), nullable=True)

def crear_usuarios():
    usuarios = [
        {'username': 'andres', 'password': 'neo123', 'es_admin':'1', 'es_empleado':'0'},
        {'username': 'martha', 'password': 'mad12345', 'es_admin':'0', 'es_empleado':'1'},
        {'username': 'david', 'password': '12345', 'es_admin':'0', 'es_empleado':'0'}
    ]

    try:
        for u in usuarios:
            usuario_existente = Usuario.query.filter_by(username=u['username']).first()
            if usuario_existente:
                print(f"El usuario '{u['username']}' ya existe. No se creará nuevamente.")
            else:
                nuevo_usuario = Usuario(username=u['username'], password=u['password'], es_admin=u['es_admin'], es_empleado=u['es_empleado'])
                db.session.add(nuevo_usuario)
        
        db.session.commit()
        print("Usuarios creados correctamente")

    except Exception as e:
        print(f"Error creando usuarios: {e}")
        db.session.rollback()