from app.models.iProducto import iProducto
from app.models.ingrediente import Ingrediente
from app.models import funciones


class Malteada(iProducto):

    def __init__(self, id: int, nombre: str, ingredientes: list[Ingrediente], precio_publico: float, volumen: int):
        self.__id = id
        self.__nombre = nombre
        self.__ingredientes = ingredientes
        self.__precio_publico = precio_publico
        self.__volumen = volumen

    def calcular_costo(self) -> float:
        return funciones.costo_produccion(self.__ingredientes) + 500

    def calcular_calorias(self) -> float:
        lista_calorias=[]
        for i in self.__ingredientes:
            lista_calorias.append(i.get_calorias())
        # 200 calorias por la crema Chantilli
        return funciones.conteo_calorias(lista_calorias)/0.95 + 200

    def calcular_rentabilidad(self) -> float                    :
        return funciones.calcular_rentabilidad_producto(self.__precio_publico, self.__ingredientes)
    
    def to_dict(self) -> dict:
        return {
            "id": self.__id,
            "tipo": "malteada",
            "nombre": self.__nombre,
            "ingredientes": [i.get_nombre() for i in self.__ingredientes],
            "precio": self.__precio_publico,
            "volumen": self.__volumen
        }

    def get_id(self) -> int:
        return self.__id
    
    def get_nombre(self) -> str:
        return self.__nombre

    def get_ingredientes(self) -> list[Ingrediente]:
        return self.__ingredientes

    def get_precio_publico(self) -> float:
        return self.__precio_publico

    def get_volumen(self) -> int:
        return self.__volumen

    def set_id(self, neo_id: int) -> None:
        self.__id = neo_id
        
    def set_nombre(self, neo_nombre: str) -> None:
        self.__nombre = neo_nombre
        
    def set_precio_publico(self, neo_precio: float) -> None:
        self.__precio_publico = neo_precio

    def set_volumen(self, neo_volumen: int) -> None:
        self.__volumen = neo_volumen
