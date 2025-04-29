from flask import Blueprint, jsonify, current_app
from flask_login import login_required

api_deploy_bp = Blueprint('api_deploy', __name__)


"""
    Parte 2 - Punto 5 | Construir el API Rest
    Construya el API completo de la heladería. El API debe permitir las siguientes operaciones:
"""

# - Consultar todos los productos.
@api_deploy_bp.route('/productos', methods=['GET'])
def all_products():
    heladeria = current_app.config.get('heladeria')
    prods = heladeria.get_productos_dict()
    return jsonify(prods)


# - Consultar un producto según su ID.
@api_deploy_bp.route('/productos/<int:id>', methods=['GET'])
def get_product(id):
    heladeria = current_app.config.get('heladeria')
    prod = heladeria.get_producto_by_id(id)
    if prod:
        return jsonify(prod.to_dict()), 200
    return jsonify({"error": "No se encontro ese producto con el ID " + str(id)}), 404


# - Consultar un producto según su nombre.
@api_deploy_bp.route('/productos/nombre/<string:nombre>', methods=['GET'])
def get_product_by_name(nombre):
    heladeria = current_app.config.get('heladeria')
    prod = heladeria.get_producto_by_name(nombre.lower())
    if prod:
        return jsonify(prod.to_dict()), 200
    return jsonify({"error": "No se encontro ese producto con el nombre " + nombre}), 404


# - Consultar las calorías de un producto según su ID.
@api_deploy_bp.route('/productos/calorias/id/<int:id>', methods=['GET'])
def get_calorias_producto(id):
    heladeria = current_app.config.get('heladeria')
    prod = heladeria.get_producto_by_id(id)
    print(type(prod))
    if prod:
        return jsonify({"nombre": prod.get_nombre(), "calorias": prod.calcular_calorias()}), 200
    return jsonify({"error": "No se encontro ese producto con el ID " + str(id)}), 404


# - Consultar la rentabilidad de un producto según su ID.
@api_deploy_bp.route('/productos/rentabilidad/id/<int:id>', methods=['GET'])
def get_rentabilidad_producto(id):
    heladeria = current_app.config.get('heladeria')
    prod = heladeria.get_producto_by_id(id)
    if prod:
        return jsonify({"nombre": prod.get_nombre(), "rentabilidad": prod.calcular_rentabilidad()}), 200
    return jsonify({"error": "No se encontro ese producto con el ID " + str(id)}), 404


# - Consultar el costo de producción de un producto según su ID.
@api_deploy_bp.route('/productos/costo_produccion/id/<int:id>', methods=['GET'])
def get_costo_produccion_producto(id):
    heladeria = current_app.config.get('heladeria')
    prod = heladeria.get_producto_by_id(id)
    if prod:
        return jsonify({"nombre": prod.get_nombre(), "costo_produccion": prod.calcular_costo()}), 200
    return jsonify({"error": "No se encontro ese producto con el ID " + str(id)}), 404


# - Vender un producto según su ID.
@api_deploy_bp.route('/productos/vender/id/<int:id>', methods=['GET'])
def vender_producto(id):
    heladeria = current_app.config.get('heladeria')
    prod = heladeria.get_producto_by_id(id)
    if prod:
        venta = heladeria.venta_de_producto(prod.get_nombre())
        if venta:
            return jsonify({"nombre": prod.get_nombre(), "Resultado": "vendido"}), 201
    return jsonify({"error": "No se encontro ese producto con el ID " + str(id)}), 404


# - Consultar todos los Ingredientes.
@api_deploy_bp.route('/ingredientes', methods=['GET'])
def all_ingredientes():
    heladeria = current_app.config.get('heladeria')
    ing = heladeria.get_ingredientes_dict()
    return jsonify(ing)


# - Consultar un ingrediente según su ID.
@api_deploy_bp.route('/ingredientes/<int:id>', methods=['GET'])
def get_ingrediente(id):
    heladeria = current_app.config.get('heladeria')
    ing = heladeria.get_ingrediente_by_id(id)
    if ing:
        return jsonify(ing.to_dict()), 200
    return jsonify({"error": "No se encontro ese ingrediente con el ID " + str(id)}), 404


# - Consultar un ingrediente según su nombre.
@api_deploy_bp.route('/ingredientes/nombre/<string:nombre>', methods=['GET'])
def get_ingrediente_by_name(nombre):
    heladeria = current_app.config.get('heladeria')
    ing = heladeria.get_ingrediente_by_name(nombre.lower())
    if ing:
        return jsonify(ing.to_dict()), 200
    return jsonify({"error": "No se encontro ese ingrediente con el nombre " + nombre}), 404


# - Consultar si un ingrediente es sano según su ID.
@api_deploy_bp.route('/ingredientes/sano/id/<int:id>', methods=['GET'])
def get_ingrediente_sano(id):
    heladeria = current_app.config.get('heladeria')
    ing = heladeria.get_ingrediente_by_id(id)
    if ing:
        return jsonify({"nombre": ing.get_nombre(), "sano": ing.es_sano()}), 200
    return jsonify({"error": "No se encontro ese ingrediente con el ID " + str(id)}), 404


# - Reabastecer un producto según su ID.
@api_deploy_bp.route('/ingredientes/reabastecer/id/<int:id>', methods=['GET'])
def reabastecer_producto(id):
    heladeria = current_app.config.get('heladeria')
    ing = heladeria.get_ingrediente_by_id(id)
    if ing:
        ing.abastecer()
        return jsonify({"nombre": ing.get_nombre(), "Resultado": "reabastecido"}), 201
    return jsonify({"error": "No se encontro ese ingrediente con el ID " + str(id)}), 404


# - Renovar el inventario de un producto según su ID
@api_deploy_bp.route('/ingredientes/renovar/id/<int:id>', methods=['GET'])
def renovar_producto(id):
    heladeria = current_app.config.get('heladeria')
    ing = heladeria.get_ingrediente_by_id(id)
    if ing:
        ing.renovar_inventario()
        return jsonify({"nombre": ing.get_nombre(), "Resultado": "renovado"}), 201
    return jsonify({"error": "No se encontro ese ingrediente con el ID " + str(id)}), 404
