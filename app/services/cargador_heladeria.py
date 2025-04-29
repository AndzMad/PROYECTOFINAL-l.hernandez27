from flask import render_template, request
from app.models.heladeria import Heladeria
from app.models.base import Base
from app.models.complemento import Complemento
from app.models.copa import Copa
from app.models.malteada import Malteada
from app.config.db import IngredientesDB, ProductosDB

def cargar_modulos_desde_BD():

    mi_heladeria = Heladeria()
    dic_ingredientes = {}
    dic_ing_js= {}
    
    ingredientes = IngredientesDB.query.all()    
    for item in ingredientes:
        if item.tipo == "base":
            ing = Base(item.id,item.nombre, item.precio, item.calorias, item.inventario, item.vegetariano, item.sabor)
            dic_ing_js[item.id] = {
                "id": item.id,
                'nombre': item.nombre,
                'tipo': item.tipo,
                'precio': item.precio,
                'calorias': item.calorias,
                'inventario': item.inventario,
                'vegetariano': item.vegetariano,
                'sabor' : item.sabor
            }
        else:
            ing = Complemento(item.id, item.nombre, item.precio, item.calorias, item.inventario, item.vegetariano)
            dic_ing_js[item.id] = {
                "id": item.id,
                'nombre': item.nombre,
                'tipo': item.tipo,
                'precio': item.precio,
                'calorias': item.calorias,
                'inventario': item.inventario,
                'vegetariano': item.vegetariano
            }
    
        dic_ingredientes[item.id] = ing
        mi_heladeria.agregar_ingrediente(ing)
        mi_heladeria.agregar_ingrediente_to_dict(dic_ing_js)

    productos = ProductosDB.query.all()
    for item in productos:

        ing1 = dic_ingredientes[item.id_ingrediente1]
        ing2 = dic_ingredientes[item.id_ingrediente2]
        ing3 = dic_ingredientes[item.id_ingrediente3]

        if item.tipo == "copa":
            pro = Copa(item.id, item.nombre, [ing1, ing2, ing3], item.precio_publico, item.tipo_vaso)
        else:
            pro = Malteada(item.id, item.nombre, [ing1, ing2, ing3], item.precio_publico, item.volumen)
 
        mi_heladeria.agregar_producto(pro)

    return mi_heladeria

