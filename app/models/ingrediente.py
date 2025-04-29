from abc import ABC, abstractmethod
from app.models import funciones


class Ingrediente(ABC):
    def __init__(self, id: int, nombre: str, precio: float, calorias: int, inventario: int, vegetariano: bool):
        self._id = id
        self._nombre = nombre
        self._precio = precio
        self._calorias = calorias
        self._inventario = inventario
        self._vegetariano = vegetariano

    def es_sano(self) -> bool:
        return funciones.esto_es_sano(self._calorias, self._vegetariano)

    @abstractmethod
    def abastecer(self) -> None:
        pass
    
    @abstractmethod
    def consumir_producto() -> None:
        pass
    
    def get_id(self) -> int:
        return self._id
    
    def get_nombre(self) -> str:
        return self._nombre

    def get_precio(self) -> float:
        return self._precio

    def get_calorias(self) -> int:
        return self._calorias

    def get_inventario(self) -> int:
        return self._inventario

    def get_vegetariano(self) -> bool:
        return self._vegetariano

    def to_dict(self) -> dict:
        return {'id': self._id,
                'nombre': self._nombre, 
                'precio' : self._precio, 
                'calorias' :self._calorias, 
                'inventario': self._inventario,
                'vegetariano': self._vegetariano}
        
    def  set_id(self, neo_id)-> None:
        self._id = neo_id
        
    def set_nombre(self, neo_nombre)-> None:
        self._nombre = neo_nombre

    def set_precio(self, neo_precio)-> None:
        self._precio = neo_precio

    def set_calorias(self, neo_calorias)-> None:
        self._calorias = neo_calorias

    def set_inventario(self, neo_inventario) -> None:
        self._inventario = neo_inventario

    def set_vegetariano(self, neo_vegetariano) -> None:
        self._vegetariano = neo_vegetariano
    
    
        
