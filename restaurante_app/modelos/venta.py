from typing import Dict, Any

class Venta:
    """Representa la relación de compra entre un usuario y un producto."""

    def __init__(self, usuario_id: str, producto_codigo: str, cantidad: int) -> None:
        if cantidad <= 0:
            raise ValueError("La cantidad de venta debe ser superior a cero.")

        self.usuario_id: str = usuario_id
        self.producto_codigo: str = producto_codigo
        self.cantidad: int = cantidad

    def a_diccionario(self) -> Dict[str, Any]:
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad
        }

    @classmethod
    def desde_diccionario(cls, datos: Dict[str, Any]) -> "Venta":
        return cls(
            usuario_id=datos["usuario_id"],
            producto_codigo=datos["producto_codigo"],
            cantidad=int(datos["cantidad"])
        )

    def mostrar_informacion(self) -> str:
        return f"Usuario ID: {self.usuario_id} | Prod Cód: {self.producto_codigo} | Cantidad: {self.cantidad}"