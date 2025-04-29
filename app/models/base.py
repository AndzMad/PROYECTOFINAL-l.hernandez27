from app.models.ingrediente import Ingrediente


class Base(Ingrediente):

    def __init__(self, id: int, nombre: str, precio: float, calorias: int, inventario: int, vegetariano: bool, sabor: str):
        super().__init__(id, nombre, precio, calorias, inventario, vegetariano)
        self.__sabor = sabor

    def abastecer(self) -> None:
        self._inventario += 5

    def consumir_producto(self) -> None:
        self._inventario= round(self._inventario - 0.2, 2)

    def get_sabor(self) -> str:
        return self.__sabor

    def set_sabor(self, neo_sabor: str) -> None:
        self.__sabor = neo_sabor
