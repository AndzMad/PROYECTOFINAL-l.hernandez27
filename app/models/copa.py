from app.models.iProducto import iProducto
from app.models.ingrediente import Ingrediente
from app.models import funciones 


class Copa(iProducto):

    def __init__(self, id: int, nombre: str, ingredientes: list[Ingrediente], precio_publico: float, tipo_vaso: str):
        self.__id = id
        self.__nombre = nombre
        self.__ingredientes = ingredientes
        self.__precio_publico = precio_publico
        self.__tipo_vaso = tipo_vaso

    def calcular_costo(self) -> float:
        return funciones.costo_produccion(self.__ingredientes)

    def calcular_calorias(self) -> float:
        lista_calorias=[]
        for i in self.__ingredientes:
            lista_calorias.append(i.get_calorias())
        return funciones.conteo_calorias(lista_calorias)

    def calcular_rentabilidad(self) -> float:
        return funciones.calcular_rentabilidad_producto(self.__precio_publico, self.__ingredientes)

    def to_dict(self) -> dict:
        return {
            "id": self.__id,
            "tipo": "copa",
            "nombre": self.__nombre,
            "ingredientes": [i.get_nombre() for i in self.__ingredientes],
            "precio": self.__precio_publico,
            "tipo_vaso": self.__tipo_vaso
        }
    
    def get_id(self) -> int:
        return self.__id
    
    def get_nombre(self) -> str:
        return self.__nombre

    def get_ingredientes(self) -> list:
        return self.__ingredientes

    def get_precio_publico(self) -> float:
        return self.__precio_publico

    def get_tipo_vaso(self) -> str:
        return self.__tipo_vaso
    
    def set_id(self, neo_id)-> None:
        self.__id = neo_id

    def set_nombre(self, neo_nombre)-> None:
        self.__nombre = neo_nombre

    def set_precio_publico(self, neo_precio) -> None:
        self.__precio_publico = neo_precio

    def set_tipo_vaso(self, neo_tipo_vaso):
        self.__tipo_vaso = neo_tipo_vaso
