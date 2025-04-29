from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_login import current_user, login_required, login_user, logout_user
from app.config.db import Usuario
from functools import wraps

home_bp = Blueprint("home", __name__)


@home_bp.route('/', methods=['GET'])
def home():
    return render_template('index.html')

def rol_requerido(rol):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if rol == 'admin' and not current_user.es_admin:
                flash("No autorizado", "danger")
                return redirect(url_for('error.no_autorizado'))
            elif rol == 'empleado' and not current_user.es_empleado:
                flash("No autorizado", "danger")
                return redirect(url_for('error.no_autorizado'))
            elif rol == 'cliente' and (current_user.es_admin or current_user.es_empleado):
                flash("No autorizado", "danger")
                return redirect(url_for('error.no_autorizado'))
            return func(*args, **kwargs)
        return wrapper
    return decorator


@home_bp.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'GET':  # Si carga la pagina por 1ra vez, muestre login.html
        return render_template('login.html')

    elif request.method == 'POST':  # Si es un POST, consulte....
        username = request.form.get('username')
        password = request.form.get('password')

        usuario = Usuario.query.filter_by(
            username=username, password=password).first()

        """
            Parte 1 - Punto 2 | Tabla Usuarios
            Implemente también un método que permita consultar en la tabla si un usuario 
            y contraseña coinciden, de modo que se pueda realizar la autenticación con 
            base al contenido de la tabla.
        """
        if (usuario):
            login_user(usuario)  # Loguea el usuario
            username = current_user.username
            flash(f"usuario {username} encontrado.", "danger")
            if usuario.es_admin == 1:
                # Si admin vamos al panel de admin
                return redirect(url_for("home.dashboard_admin"))
            else:
                return redirect(url_for('home.dashboard'))

        # Si no encuentra al usuario retorna al login
        flash("Las credenciales son incorrectas.", "danger")
        return redirect(url_for("home.login"))


@home_bp.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    username = current_user.username
    return render_template('dashboard.html', username=username)


@home_bp.route('/dashboard_admin', methods=['GET'])
@login_required
@rol_requerido('admin')
def dashboard_admin():
    username = current_user.username
    return render_template('dashboard_admin.html', username=username)


@home_bp.route('/dashboard_cliente', methods=['GET'])
@login_required
def dashboard_cliente():
    username = current_user.username
    return render_template('dashboard_cliente.html', username=username)


@home_bp.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for("home.login"))


@home_bp.route('/no_autorizado', methods=['GET'])
def no_autorizado():
    return render_template('no_autorizado.html'), 401


@home_bp.route("/auth/profile")
@login_required  # Se requiere que el usuario este logueado
def profile():
    print(current_user.__dict__)
    return render_template(f'perfil.html')


@home_bp.route("/tienda", methods=['GET'])
@login_required
def tienda():
    heladeria = current_app.config.get('heladeria')
    productos = heladeria.get_productos()
    return render_template("tienda.html", productos=productos)


@home_bp.route("/venta_producto", methods=['GET'])
@login_required
def venta_producto():
    nombre_producto = request.args.get("nombre")
    heladeria = current_app.config.get('heladeria')
    try:
        resultado_venta = heladeria.venta_de_producto(nombre_producto)
    except ValueError as e:
        resultado_venta = f"¡Oh no! Nos hemos quedado sin {str(e)} 😕"
    return render_template("venta_producto.html", nombre=nombre_producto, resultado_venta=resultado_venta)


@home_bp.route('/productosh', methods=['GET'])
@login_required
def productos_html():
    heladeria = current_app.config.get('heladeria')
    productos = heladeria.get_productos_dict()
    return render_template('productos.html', productos=productos)


@home_bp.route("/calorias_todos_productos", methods=['GET'])
@login_required
def calorias_todos_productos():
    heladeria = current_app.config.get('heladeria')
    productos = heladeria.get_productos()  # Obtener todos los productos
    calorias = []

    for producto in productos:
        calorias.append({
            'nombre': producto.get_nombre(),
            'calorias': producto.calcular_calorias()
        })

    return render_template("calorias_todos_productos.html", calorias=calorias)


@home_bp.route("/rentabilidad_productos", methods=['GET'])
@login_required
def rentabilidad_productos():
    heladeria = current_app.config.get('heladeria')
    productos = heladeria.get_productos()

    # Calcular rentabilidad de todos los productos
    productos_rentabilidad = []
    for producto in productos:
        productos_rentabilidad.append({
            "nombre": producto.get_nombre(),
            "rentabilidad": producto.calcular_rentabilidad()
        })

    return render_template('rentabilidad_productos.html', productos_rentabilidad=productos_rentabilidad)


@home_bp.route('/costo_produccion_productos', methods=['GET'])
@login_required
def costo_produccion_productos():
    heladeria = current_app.config.get('heladeria')
    productos = heladeria.get_productos()
    productos_costo = []

    for producto in productos:
        costo = producto.calcular_costo()
        productos_costo.append({
            "nombre": producto.get_nombre(),
            "costo_produccion": costo
        })

    return render_template('costo_produccion_productos.html', productos_costo=productos_costo)


@home_bp.route("/ingredientes_web", methods=["GET"])
@login_required
def ingredientes_view():
    heladeria = current_app.config.get('heladeria')
    ingredientes = heladeria.get_ingredientes_dict()
    return render_template("ingredientes_web.html", ingredientes=ingredientes)


@home_bp.route("/reabastecer_ingredientes", methods=["GET", "POST"])
@login_required
def reabastecer_ingredientes():
    heladeria = current_app.config.get('heladeria')

    # Si es un POST, se reabastecerán todos los ingredientes
    if request.method == "POST":
        ingredientes = heladeria.get_ingredientes()
        for ingrediente in ingredientes:
            ingrediente.abastecer()  # Abastecer cada ingrediente
        flash("Todos los ingredientes han sido reabastecidos.", "success")
        return redirect(url_for("home.reabastecer_ingredientes"))

    ingredientes = heladeria.get_ingredientes_dict()
    return render_template("reabastecer_ingredientes.html", ingredientes=ingredientes)
