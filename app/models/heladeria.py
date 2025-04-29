from app.models import funciones
from app.models.base import Base
from app.models.complemento import Complemento


class Heladeria():

    def __init__(self):
        self.__productos = []
        # self.__productos_dict = {}
        self.__ingredientes = []
        self.__ingredientes_dict = {}
        self.__ventas = 0

    def agregar_producto(self, producto) -> None:
        self.__productos.append(producto)

    def agregar_ingrediente(self, ingrediente) -> None:
        self.__ingredientes.append(ingrediente)

    def agregar_ingrediente_to_dict(self, ingrediente_dicc) -> None:
        self.__ingredientes_dict = ingrediente_dicc

    def producto_mas_rentable(self) -> str:
        return funciones.producto_mas_rentable(self.__productos)

    def venta_de_producto(self, nombre_producto: str) -> bool:
        for producto in self.__productos:
            if producto.get_nombre() == nombre_producto:
                for ingrediente in producto.get_ingredientes():
                    if isinstance(ingrediente, Base) and ingrediente._inventario < 0.2:
                        raise ValueError(ingrediente.get_nombre())

                    if isinstance(ingrediente, Complemento) and ingrediente._inventario < 0.2:
                        raise ValueError(ingrediente.get_nombre())

                    ingrediente.consumir_producto()

                valor_producto = producto.get_precio_publico()

        self.ventas_del_dia(valor_producto)
        print(f"Venta exitosa de {nombre_producto}")
        print(f"Ventas del día ${self.__ventas}")
        return "¡Vendido!"

    def ventas_del_dia(self, venta_producto) -> None:
        self.__ventas += venta_producto

    def get_productos(self) -> list:
        return self.__productos

    def get_productos_dict(self) -> list:
        dict_productos = {}
        for i in self.__productos:
            dict_productos[i.get_id()] = i.to_dict()
        return dict_productos
            
    def get_producto_by_id(self, id: int) -> str:
        for i in self.__productos:
            if i.get_id() == id:
                return i
        return None

    def get_producto_by_name(self, nombre: str) -> str:
        for i in self.__productos:
            if i.get_nombre().lower() == nombre:
                return i
                
    def get_ingrediente_by_name(self, nombre: str) -> str:
        for i in self.__ingredientes:
            if i.get_nombre().lower() == nombre:
                return i

    def get_ingrediente_by_id(self, id: int) -> str:
        for ingrediente in self.__ingredientes:
            if ingrediente.get_id() == id:
                return ingrediente
        return None

    def get_ingredientes(self) -> list:
        return self.__ingredientes

    def get_ingredientes_dict(self) -> list:
        return self.__ingredientes_dict

    def get_ventas_del_dia(self) -> float:
        return self.__ventas

