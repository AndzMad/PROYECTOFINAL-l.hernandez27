from app.models.ingrediente import Ingrediente


class Complemento(Ingrediente):

    def __init__(self, id: int, nombre: str, precio: float, calorias: int, inventario: float, vegetariano: bool):
        super().__init__(id, nombre, precio, calorias, inventario, vegetariano)

    def renovar_inventario(self) -> None:
        self._inventario = 0

    def consumir_producto(self) -> None:
        self._inventario -= 1

    def abastecer(self) -> None:
        self._inventario += 10
